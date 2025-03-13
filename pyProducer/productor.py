import os
import pika
from flask import Flask, request

# Leer variables de entorno
RABBITMQ_USER = os.environ.get("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "guest")
RABBITMQ_EXCHANGE = os.environ.get("RABBITMQ_EXCHANGE", '')
RABBITMQ_QUEUE = os.environ.get("RABBITMQ_QUEUE", '')
RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.environ.get("RABBITMQ_PORT", 5672))
FLASK_PORT = int(os.environ.get("FLASK_PORT", 5051))


# 1. Conectar a RabbitMQ
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters(
    host=RABBITMQ_HOST,
    port=RABBITMQ_PORT,
    credentials=credentials
)
try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    print("¡Conexión exitosa!")
except Exception as e:
    print(f"Error de conexión: {e}")



# 3. Publicar un mensaje en la cola
def enviar(mensaje):
    print(f"Publicando: {mensaje}")
    channel.basic_publish(
        exchange=RABBITMQ_EXCHANGE,  # Usar el exchange deseado
        routing_key=RABBITMQ_QUEUE,  # Nombre de la cola
        body=mensaje,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Hacer el mensaje persistente
        )
    )



# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta para enviar un mensaje
@app.route('/enviar', methods=['GET'])
def enviar_mensaje():
    # Obtener el mensaje
    mensaje = request.args.get('msg', '').strip()
    enviar(mensaje)
    return f"Se envió: {mensaje}"

@app.route('/reconect', methods=['GET'])
def reconect():
    global connection
    global channel
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        print("¡Conexión exitosa!")
        return "¡Conexión exitosa!"
    except Exception as e:
        print(f"Error de conexión: {e}")
        return f"Estado: {e}"

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(port=FLASK_PORT, debug=True)



# 4. Cerrar la conexión
connection.close()
import os
import pika
import threading
from flask import Flask, request

# Leer variables de entorno
RABBITMQ_USER = os.environ.get("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "guest")
RABBITMQ_QUEUE = os.environ.get("RABBITMQ_QUEUE", '')
RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.environ.get("RABBITMQ_PORT", 5672))
FLASK_PORT = int(os.environ.get("FLASK_PORT", 5052))

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


mensajesRecibidos = "Recibidos:"
# Y un lock para sincronizar el acceso a dicha lista
lock = threading.Lock()

# 3. Definir una función para procesar los mensajes
def callback(ch, method, properties, body):
    mensaje = body.decode()
    print(f"[x] Recibido: {mensaje}")
    with lock:
        global mensajesRecibidos
        mensajesRecibidos = mensajesRecibidos + "<br> - " + mensaje
    # Marcar el mensaje como procesado
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Configura el prefetch count para controlar el número de mensajes que el cliente consume antes de recibir más
channel.basic_qos(prefetch_count=1000)  # <--- ¡Clave para streams!

# 4. Configurar el consumer
channel.basic_consume(
    queue=RABBITMQ_QUEUE,
    on_message_callback=callback,
    auto_ack=False  # Desactivar auto-ack para manejar manualmente
)
def consumir_mensajes():
    channel.start_consuming()




# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta para obtener mensajes (GET)
@app.route('/mensaje', methods=['GET'])
def obtener_mensajes():
    # Se adquiere el lock para leer de forma segura
    with lock:
        mensajes_html = mensajesRecibidos
    return mensajes_html

# 5. Iniciar Flask en un hilo separado
if __name__ == '__main__':
    # Crear un hilo para consumir mensajes
    hilo_rabbitmq = threading.Thread(target=consumir_mensajes, daemon=True)
    hilo_rabbitmq.start()

    # Iniciar Flask en el hilo principal
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=True)
import pika

# 1. Conectar a RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
    host='10.6.101.102',
    port=5672
)
try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    print("¡Conexión exitosa!")
except Exception as e:
    print(f"Error de conexión: {e}")

# 3. Publicar un mensaje en la cola

def enviar():
    while(True):
        mensaje = input()
        if mensaje == "exit":
            break

        channel.basic_publish(
            exchange='fanoutExchange',  # Usar el exchange deseado
            routing_key='fanoutQueue',  # Nombre de la cola
            body=mensaje,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Hacer el mensaje persistente
            )
        )
        print(f"Enviado: {mensaje}")

enviar()

# 4. Cerrar la conexión
connection.close()
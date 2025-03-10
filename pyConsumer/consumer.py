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


# 3. Definir una función para procesar los mensajes
def callback(ch, method, properties, body):
    print(f"[x] Recibido: {body.decode()}")
    # Marcar el mensaje como procesado
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Configura el prefetch count para controlar el número de mensajes que el cliente consume antes de recibir más
channel.basic_qos(prefetch_count=1000)  # <--- ¡Clave para streams!

# 4. Configurar el consumer
channel.basic_consume(
    queue='pyqueue',
    on_message_callback=callback,
    auto_ack=False  # Desactivar auto-ack para manejar manualmente
)

print('[*] Esperando mensajes. Presiona CTRL+C para salir.')

# 5. Iniciar el consumo de mensajes
channel.start_consuming()
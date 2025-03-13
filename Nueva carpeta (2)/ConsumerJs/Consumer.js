const amqp = require('amqplib');

const RABBITMQ_HOST = process.env.RABBITMQ_HOST || 'rabbitmqt';
const RABBITMQ_URL = `amqp://admin:admin@${RABBITMQ_HOST}:5672`;
const EXCHANGE_NAME = 'fanoutExchange';
const EXCHANGE_TYPE = 'fanout';

async function startConsumer() {
  try {
    // Conecta a RabbitMQ y crea un canal
    const connection = await amqp.connect(RABBITMQ_URL);
    const channel = await connection.createChannel();

    // Declara el exchange fanout
    await channel.assertExchange(EXCHANGE_NAME, EXCHANGE_TYPE, { durable: true });

    // Crea una cola exclusiva y temporal
    const q = await channel.assertQueue('', { exclusive: true });
    
    // Vincula la cola al exchange
    await channel.bindQueue(q.queue, EXCHANGE_NAME, '');
    
    console.log("Esperando mensajes...");
    channel.consume(q.queue, msg => {
      if (msg !== null) {
        console.log("Mensaje recibido:", msg.content.toString());
      }
    }, { noAck: true });
    
  } catch (error) {
    console.error("Error en consumer:", error);
  }
}

startConsumer();

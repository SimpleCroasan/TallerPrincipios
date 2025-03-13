const express = require('express');
const amqp = require('amqplib');

const app = express();
const PORT = 8083;
const RABBITMQ_HOST = process.env.RABBITMQ_HOST || 'rabbitmqt';
const RABBITMQ_URL = `amqp://admin:admin@${RABBITMQ_HOST}:5672`;
const EXCHANGE_NAME = 'fanoutExchange';
const EXCHANGE_TYPE = 'fanout';

let channel;

// Función para conectar a RabbitMQ y crear el canal
async function connectRabbitMQ() {
  try {
    const connection = await amqp.connect(RABBITMQ_URL);
    channel = await connection.createChannel();
    await channel.assertExchange(EXCHANGE_NAME, EXCHANGE_TYPE, { durable: true });
    console.log("Conectado a RabbitMQ y exchange creado");
  } catch (error) {
    console.error("Error al conectar a RabbitMQ:", error);
  }
}

connectRabbitMQ();

app.get('/', (req, res) => {
  const message = req.query.message;
  if (!message) {
    return res.status(400).send("Falta el parámetro 'message'");
  }
  try {
    
    channel.publish(EXCHANGE_NAME, '', Buffer.from(message));
    console.log(`Mensaje enviado: ${message}`);
    res.send(`Mensaje enviado: ${message}`);
  } catch (error) {
    console.error("Error al enviar el mensaje:", error);
    res.status(500).send("Error al enviar el mensaje");
  }
});

app.listen(PORT, () => {
  console.log(`Producer escuchando en el puerto ${PORT}`);
});

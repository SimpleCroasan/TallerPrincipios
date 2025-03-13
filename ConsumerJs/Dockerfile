
FROM node:20

WORKDIR /app


COPY Consumer.js .

RUN npm init -y && npm install express amqplib


EXPOSE 8084

CMD ["node", "Consumer.js"]

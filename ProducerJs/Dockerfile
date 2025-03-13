
FROM node:20


WORKDIR /app


COPY Producer.js .

RUN npm init -y && npm install express amqplib


EXPOSE 8083


CMD ["node", "Producer.js"]

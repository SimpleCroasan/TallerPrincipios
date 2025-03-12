package producer.rabb.demo;

import lombok.extern.slf4j.Slf4j;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
@Slf4j
public class ConsumerListener {

    @RabbitListener(queues = RabbitConfig.QUEUE_NAME)
    public void receiveMessageJava(String message) {
        log.info("Mensaje recibido en ConsumerJava: " + message);
    }


    @RabbitListener(queues = RabbitConfig.QUEUE_NAME_2)
    public void receiveMessageJava2(String message) {
        log.info("Mensaje recibido en ConsumerJava2: " + message);
    }

    @RabbitListener(queues = RabbitConfig.QUEUE_NAME_3)
    public void receiveMessageJava3(String message) {
        log.info("Mensaje recibido en ConsumerJava3: " + message);
    }
}
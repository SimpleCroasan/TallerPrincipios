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
}
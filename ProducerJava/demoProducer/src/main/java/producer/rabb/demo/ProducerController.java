package producer.rabb.demo;

import lombok.extern.slf4j.Slf4j;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@Slf4j
public class ProducerController {

    private final RabbitTemplate rabbitTemplate;

    public ProducerController(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    @GetMapping("/send")
    public ResponseEntity<String> sendMessage(@RequestParam(name = "message") String message) {

        rabbitTemplate.convertAndSend(RabbitConfig.FANOUT_EXCHANGE, "", message);
        log.info(message);
        return ResponseEntity.ok("Mensaje enviado: " + message);
    }
}

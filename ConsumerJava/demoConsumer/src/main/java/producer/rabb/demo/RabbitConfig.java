package producer.rabb.demo;

import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.core.FanoutExchange;
import org.springframework.amqp.core.Queue;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitConfig {

    public static final String FANOUT_EXCHANGE = "fanoutExchange";
    public static final String QUEUE_NAME = "fanoutQueue";
    public static final String QUEUE_NAME_2 = "fanoutQueue2";
    public static final String QUEUE_NAME_3 = "fanoutQueue3";

    @Bean
    public FanoutExchange fanoutExchange() {
        return new FanoutExchange(FANOUT_EXCHANGE);
    }

    @Bean
    public Queue queue() {
        return new Queue(QUEUE_NAME);
    }


    @Bean
    public Queue queue2() {
        return new Queue(QUEUE_NAME_2);
    }


    @Bean
    public Queue queu3() {
        return new Queue(QUEUE_NAME_3);
    }

    @Bean
    public Binding binding(FanoutExchange fanoutExchange, Queue queue) {
        // En un exchange fanout, el routingKey se ignora
        return BindingBuilder.bind(queue).to(fanoutExchange);
    }
}
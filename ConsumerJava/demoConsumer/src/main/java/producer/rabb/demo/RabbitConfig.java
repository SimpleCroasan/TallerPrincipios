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

    @Bean
    public FanoutExchange fanoutExchange() {
        return new FanoutExchange(FANOUT_EXCHANGE);
    }

    @Bean
    public Queue queue() {
        return new Queue(QUEUE_NAME);
    }

    @Bean
    public Binding binding(FanoutExchange fanoutExchange, Queue queue) {
        // En un exchange fanout, el routingKey se ignora
        return BindingBuilder.bind(queue).to(fanoutExchange);
    }
}
package producer.rabb.demo;

import org.springframework.amqp.core.FanoutExchange;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

// Producer: RabbitConfig.java
@Configuration
public class RabbitConfig {

    public static final String FANOUT_EXCHANGE = "fanoutExchange";

    @Bean
    public FanoutExchange fanoutExchange() {
        return new FanoutExchange(FANOUT_EXCHANGE);
    }
}

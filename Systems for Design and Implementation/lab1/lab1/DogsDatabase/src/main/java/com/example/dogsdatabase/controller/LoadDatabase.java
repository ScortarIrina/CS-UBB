package com.example.dogsdatabase.controller;

import com.example.dogsdatabase.model.Dog;
import com.example.dogsdatabase.repository.DogRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
class LoadDatabase {

    private static final Logger log = LoggerFactory.getLogger(LoadDatabase.class);

    @Bean
    CommandLineRunner initDatabase(DogRepository repository) {

        return args -> {
            log.info("Preloading " + repository.save(new Dog("Benji", "Beagle", 11, 20, "John")));
            log.info("Preloading " + repository.save(new Dog("Nino", "mix-breed", 6, 22, "Paul")));
            log.info("Preloading " + repository.save(new Dog("Lizzie", "Poodle", 1, 12, "Lucy")));
            log.info("Preloading " + repository.save(new Dog("Tommy", "Labrador", 4, 29, "Hans")));
            log.info("Preloading " + repository.save(new Dog("Zorro", "Boxer", 3, 40, "Mary")));
            log.info("Preloading " + repository.save(new Dog("Loki", "Yorkshire Terrier", 13, 4, "Doris")));
        };
    }
}

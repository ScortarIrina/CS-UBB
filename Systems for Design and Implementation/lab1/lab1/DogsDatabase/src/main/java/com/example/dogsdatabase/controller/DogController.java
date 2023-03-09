package com.example.dogsdatabase.controller;

import com.example.dogsdatabase.exceptions.DogNotFoundException;
import com.example.dogsdatabase.model.Dog;
import com.example.dogsdatabase.repository.DogRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class DogController {

    private final DogRepository repository;

    DogController(DogRepository repository) {
        this.repository = repository;
    }

    // localhost:8080/dogs
    @GetMapping("/dogs")
    List<Dog> getAllDogs() {
        return repository.findAll();
    }

    @PostMapping("/dogs")
    Dog addDog(@RequestBody Dog newDog) {
        return this.repository.save(newDog);
    }

    @GetMapping("/dogs/{id}")
    Dog one(@PathVariable Long id) {

        return repository.findById(id)
                .orElseThrow(() -> new DogNotFoundException(id));
    }

    @PutMapping("/dogs/{id}")
    Dog updateDog(@RequestBody Dog newDog, @PathVariable Long id) {

        return repository.findById(id)
                .map(dog -> {
                    dog.setName(newDog.getName());
                    dog.setAge(newDog.getAge());
                    dog.setBreed(newDog.getBreed());
                    dog.setWeight(newDog.getWeight());
                    dog.setOwner(newDog.getOwner());
                    return repository.save(dog);
                })
                .orElseGet(() -> {
                    newDog.setId(id);
                    return repository.save(newDog);
                });
    }

    @DeleteMapping("/dogs/{id}")
    void deleteDog(@PathVariable Long id) {
        repository.deleteById(id);
    }
}

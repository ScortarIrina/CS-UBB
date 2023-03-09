package com.example.dogsdatabase.repository;

import com.example.dogsdatabase.model.Dog;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DogRepository extends JpaRepository<Dog, Long> {
}

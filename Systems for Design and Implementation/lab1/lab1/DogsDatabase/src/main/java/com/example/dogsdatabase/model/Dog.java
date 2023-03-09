package com.example.dogsdatabase.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

import java.util.Objects;

@Entity
public class Dog {

    private @Id @GeneratedValue Long id;
    private String name;
    private String breed;
    private int age;
    private int weight;
    private String owner;

    public Dog() {
    }

    public Dog(String name, String breed, int age, int weight, String owner) {
        this.name = name;
        this.breed = breed;
        this.age = age;
        this.weight = weight;
        this.owner = owner;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.id, this.name, this.breed, this.age, this.weight, this.owner);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Dog)) return false;
        Dog dog = (Dog) obj;
        return Objects.equals(this.id, dog.id) &&
                Objects.equals(this.name, dog.name) &&
                Objects.equals(this.age, dog.age) &&
                Objects.equals(this.breed, dog.breed) &&
                Objects.equals(this.weight, dog.weight) &&
                Objects.equals(this.owner, dog.owner);
    }

    @Override
    public String toString() {
        return "Dog{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", breed='" + breed + '\'' +
                ", age=" + age +
                ", weight=" + weight +
                ", owner='" + owner + '\'' +
                '}';
    }
}

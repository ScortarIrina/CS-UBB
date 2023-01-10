package Model;

public class Pig extends Entity {

    private String breed;
    private int age;

    public Pig(String breed, int age) {
        this.breed = breed;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Pig{" +
                "breed='" + breed + '\'' +
                ", age=" + age +
                ", weight=" + weight +
                '}';
    }
}

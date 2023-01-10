package Model;

public class Bird extends Entity {

    private String type;
    private String gender;

    public Bird(String type, String gender) {
        this.type = type;
        this.gender = gender;
    }

    @Override
    public String toString() {
        return "Bird{" +
                "type='" + type + '\'' +
                ", gender='" + gender + '\'' +
                ", weight=" + weight +
                '}';
    }
}

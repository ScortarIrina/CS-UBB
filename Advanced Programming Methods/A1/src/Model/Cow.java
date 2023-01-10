package Model;

public class Cow extends Entity {

    private String colour;
    private String name;

    public Cow(String colour, String name) {
        this.colour = colour;
        this.name = name;
    }

    @Override
    public String toString() {
        return "Cow{" +
                "colour='" + colour + '\'' +
                ", name='" + name + '\'' +
                ", weight=" + weight +
                '}';
    }
}

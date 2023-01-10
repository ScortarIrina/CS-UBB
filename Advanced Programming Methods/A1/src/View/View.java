package View;

import Controller.Controller;
import Model.Entity;
import Model.Bird;
import Model.Cow;
import Model.Pig;

public class View {

    Controller controller;

    public View(Controller controller) {
        this.controller = controller;
    }

    public void execute() {

        Entity pig1 = new Pig("Berkshire", 3);
        pig1.setWeight(120);
        controller.add(pig1);

        Entity cow1 = new Cow("white", "Milka");
        cow1.setWeight(200);
        controller.add(cow1);

        Entity rooster = new Bird("rooster", "male");
        rooster.setWeight(4);
        controller.add(rooster);

        Entity duck = new Bird("duck", "female");
        duck.setWeight(2);
        controller.add(duck);

        Entity pig2 = new Pig("Chester White", 2);
        pig2.setWeight(130);
        controller.add(pig2);

        Entity chicken = new Bird("chicken", "male");
        chicken.setWeight(1);
        controller.add(chicken);

        Entity[] filteredEntities = controller.getEntitiesHeavierThan3kg();
        Entity[] entities = controller.getAll();

        int lenEntities = controller.getLengthAllEntities();
        int lenFilteredEntities = controller.getLengthFilteredEntities();

        System.out.println("");
        System.out.println("All animals:");
        for (int i = 0; i < lenEntities; i++) {
            System.out.println("   " + entities[i]);
        }
        System.out.println("");

        System.out.println("Animals heavier tha 3 kg:");
        for (int i = 0; i < lenFilteredEntities; i++) {
            System.out.println("   " + filteredEntities[i]);
        }
        System.out.println("");

        System.out.println("After removing an animal:");
        controller.remove(cow1);
        int newLenEntities = controller.getLengthAllEntities();
        for (int i = 0; i < newLenEntities; i++) {
            System.out.println("   " + entities[i]);
        }
        System.out.println("");
    }
}

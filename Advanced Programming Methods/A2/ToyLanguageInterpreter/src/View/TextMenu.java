package View;

import Exceptions.ADTException;
import Model.ADTs.MyDictionary;
import Model.ADTs.IDictionary;

import java.util.Scanner;

public class TextMenu {
    private IDictionary<String,Command> commands;

    public TextMenu() {
        this.commands = new MyDictionary<>();
    }
    
    public void addCommand(Command c) {
        commands.put(c.getKey(),c);
    }
    
    private void displayMenu() {
        for(Command c: commands.values()) {
            String line = String.format("%4s:%s", c.getKey(),c.getDescription());
            System.out.println(line);
        }
    }

    public void show() {
        Scanner s = new Scanner(System.in);

        while(true) {
            System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
            displayMenu();
            System.out.println("\nChoose an option: ");
            String key = s.nextLine();
            try {
                Command c = commands.search(key);
                c.execute();
            }
            catch(ADTException e) {
                System.out.println("Invalid option");
            }
        }
    }
}

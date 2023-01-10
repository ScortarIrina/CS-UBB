/*
    4. La o ferma se cresc pasari, vaci si porci.
    Sa se afiseze toate animalele care au greutatea
    mai mare decat 3kg.
 */


import Controller.Controller;
import Repository.Repository;
import Repository.IRepository;
import View.View;

public class Main {
    public static void main(String[] args) {
        IRepository repository = new Repository();
        Controller controller = new Controller(repository);
        View view = new View(controller);
        view.execute();
    }
}
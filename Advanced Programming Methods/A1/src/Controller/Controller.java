package Controller;

import Repository.IRepository;
import Exceptions.NegativeWeightException;
import Model.Entity;


public class Controller {

    IRepository repository;

    public Controller(IRepository repository) {
        this.repository = repository;
    }

    public void add(Entity entity) {
        try {
            repository.add(entity);
        }
        catch (NegativeWeightException e) {
            System.out.println("Negative weight error!");
        }
    }

    public void remove(Entity entity) {
        repository.remove(entity);
    }

    public Entity[] getAll() {
        return repository.getAll();
    }

    public int getLengthAllEntities() {
        return repository.getLengthAllEntities();
    }

    public int getLengthFilteredEntities() {
        return repository.getLengthFilteredEntities();
    }

    public Entity[] getEntitiesHeavierThan3kg() {
        return repository.getAllWithWeightGreaterThan();
    }
}

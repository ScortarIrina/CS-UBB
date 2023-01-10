package Repository;

import Exceptions.NegativeWeightException;
import Model.Entity;


public class Repository implements IRepository {

    private Entity[] entities;

    private int size;

    private int sizeFiltered;

    public Repository() {
        entities = new Entity[100];
        size = 0;
        sizeFiltered = 0;
    }

    @Override
    public void add(Entity entity) throws NegativeWeightException {
        if (entity.getWeight() <= 0) {
            throw new NegativeWeightException();
        }
        entities[size] = entity;
        size++;
    }

    @Override
    public void remove(Entity entity) {
        for (int i = 0; i < size-1; i++) {
            if (entity == entities[i]) {
                for (int j = i; j < size; j++) {
                    entities[j] = entities[j+1];
                }
                size--;
            }
        }
        if (entity == entities[size-1]) {
            size--;
        }
    }

    @Override
    public int getLengthAllEntities() {
        return size;
    }

    @Override
    public Entity[] getAll() {
        return entities;
    }

    @Override
    public Entity[] getAllWithWeightGreaterThan() {
        Entity[] filterEntities = new Entity[100];
        int i = -1;

        for (int index = 0; index < size; index++) {
            Entity entity = entities[index];
            if (entity.getWeight() >= 3) {
                filterEntities[++i] = entity;
                sizeFiltered++;
            }
        }
        return filterEntities;
    }

    @Override
    public int getLengthFilteredEntities() {
        return sizeFiltered;
    }
}

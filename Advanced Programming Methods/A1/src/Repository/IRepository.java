package Repository;

import Exceptions.NegativeWeightException;
import Model.Entity;


public interface IRepository {

    void add(Entity entity) throws NegativeWeightException;

    void remove(Entity entity);

    Entity[] getAll();

    Entity[] getAllWithWeightGreaterThan() ;

    int getLengthAllEntities();

    int getLengthFilteredEntities();
}

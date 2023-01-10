package Model.ADTs;

import Exceptions.ADTException;

import java.util.Collection;
import java.util.Map;
import java.util.Set;

public interface IDictionary<TKey, TValue> {

    void put(TKey k, TValue v);

    boolean exists(TKey k);

    void remove(TKey k) throws ADTException;

    TValue search(TKey k) throws ADTException;

    void update(TKey k, TValue v);

    Set<TKey> getAllKeys();

    public Map<TKey, TValue> getAll();

    Collection<TValue> values();

    String dictToString() throws ADTException;

    Map<TKey, TValue> getContent();

    IDictionary<TKey, TValue> deepCopy() throws ADTException;
}

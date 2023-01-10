package Model.ADTs;

import Exceptions.ADTException;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MyDictionary<TKey,TValue> implements IDictionary<TKey, TValue> {
    HashMap<TKey,TValue> dictionary;

    public MyDictionary() {
        this.dictionary = new HashMap<>();
    }

    @Override
    public void put(TKey k, TValue v) {
        this.dictionary.put(k,v);
    }

    @Override
    public boolean exists(TKey k) {
        return this.dictionary.containsKey(k);
    }

    @Override
    public void remove(TKey k) throws ADTException {
        if(!exists(k))
            throw new ADTException("Key doesn't exist");
        this.dictionary.remove(k);
    }

    @Override
    public TValue search(TKey k) throws ADTException {
        if(!exists(k))
            throw new ADTException("Key is not defined");
        else
            return this.dictionary.get(k);
    }

    @Override
    public Map<TKey, TValue> getAll() {
        return this.dictionary;
    }

    @Override
    public void update(TKey k, TValue v) {
        this.dictionary.put(k,v);
    }

    @Override
    public Set<TKey> getAllKeys() {
        return dictionary.keySet();
    }

    public String dictToString() throws ADTException {
        String str = "";
        for(TKey key: getAllKeys()) {
            str = str+" "+key+": "+search(key)+"\n";
        }
        return str;
    }

    @Override
    public Map<TKey, TValue> getContent() {
        return dictionary;
    }

    @Override
    public IDictionary<TKey, TValue> deepCopy() throws ADTException {
        IDictionary<TKey, TValue> toReturn = new MyDictionary<>();
        for (TKey key : getAllKeys()) {
            toReturn.put(key, search(key));
        }
        return toReturn;
    }

    @Override
    public Collection<TValue> values() {
        return this.dictionary.values();
    }
}

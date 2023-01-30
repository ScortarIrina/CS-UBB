package com.example.a7gui.Model.ADTs;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MyDictionary<TKey, TValue> implements IDictionary<TKey, TValue> {

    HashMap<TKey, TValue> dictionary;

    public MyDictionary() {
        this.dictionary = new HashMap<>();
    }

    @Override
    public void put(TKey k, TValue v) {
        this.dictionary.put(k, v);
    }

    @Override
    public boolean exists(TKey k) {
        return this.dictionary.containsKey(k);
    }

    @Override
    public void remove(TKey k) throws InterpreterException {
        if (!exists(k))
            throw new InterpreterException("ERROR: Key does not exist!");
        this.dictionary.remove(k);
    }

    @Override
    public TValue search(TKey k) throws InterpreterException {
        if (!exists(k))
            throw new InterpreterException("ERROR: Key is not defined!");
        return this.dictionary.get(k);
    }

    @Override
    public void update(TKey k, TValue v) {
        this.dictionary.put(k, v);
    }

    @Override
    public Set<TKey> getAllKeys() {
        return dictionary.keySet();
    }

    @Override
    public Map<TKey, TValue> getAll() {
        return this.dictionary;
    }

    @Override
    public Collection<TValue> values() {
        return this.dictionary.values();
    }

    @Override
    public String dictToString() throws InterpreterException {
        String string = "";
        for (TKey key : getAllKeys()) {
            string = string + " " + key + search(key) + "\n";
        }
        return string;
    }

    @Override
    public Map<TKey, TValue> getContent() {
        return this.dictionary;
    }

    @Override
    public IDictionary<TKey, TValue> deepCopy() throws InterpreterException {
        IDictionary<TKey, TValue> toReturn = new MyDictionary<>();
        for (TKey key : getAllKeys()) {
            toReturn.put(key, search(key));
        }
        return toReturn;
    }
}

package com.example.a7gui.Model.ADTs;

import com.example.a7gui.Exceptions.InterpreterException;
import java.util.Collection;
import java.util.Map;
import java.util.Set;

public interface IDictionary<TKey, TValue> {

    // adds a <key, value> pair to the dictionary
    void put(TKey k, TValue v);

    // checks whether the key k exists in the dictionary
    boolean exists(TKey k);

    // removes the pair with key k from the dictionary
    void remove(TKey k) throws InterpreterException;

    // searches for the value of key k and returns its value
    TValue search(TKey k) throws InterpreterException;

    // changes the value corresponding to key k with value v
    void update(TKey k, TValue v);

    // returns all the keys from the dictionary as a set
    Set<TKey> getAllKeys();

    // returns all <key, value> pairs from the dictionary as a Map
    public Map<TKey, TValue> getAll();

    // returns all the values in the dictionary as a collection
    Collection<TValue> values();

    // converts a dictionary to a string
    String dictToString() throws InterpreterException;

    Map<TKey, TValue> getContent();

    IDictionary<TKey, TValue> deepCopy() throws InterpreterException;
}

package com.example.a7gui.Model.ADTs;

import com.example.a7gui.Model.Types.IntType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.Values.IntValue;

import java.util.HashMap;
import java.util.Set;

public interface IHeap {

    int getFreeValue();

    // returns the content of the heap
    HashMap<Integer, IValue> getContent();

    // sets the content of the heap
    void setContent(HashMap<Integer, IValue> newMap);

    // adds a new value to the heap
    int add(IValue value);

    // updates the position in the heap to a new value
    void update(Integer position, IValue value) throws InterpreterException;

    // gets the value from a given position
    IValue get(Integer position) throws InterpreterException;

    // checks if the heap contains a key
    boolean containsKey(Integer position);

    // removes a key from the heap
    void remove(Integer key) throws InterpreterException;

    // returns the keys in the heap as a set of integers
    Set<Integer> keySet();
}

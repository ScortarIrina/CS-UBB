package Model.ADTs;

import Exceptions.ADTException;
import Model.Values.IValue;

import java.util.HashMap;
import java.util.Set;

public interface IHeap {

    int getFreeValue();

    // return the content of the heap
    HashMap<Integer, IValue> getContent();

    // set the content of the heap
    void setContent(HashMap<Integer, IValue> newMap);

    // add a new value in the heap
    int add(IValue value);

    // update the position in the heap to a new value
    void update(Integer position, IValue value) throws ADTException;

    IValue get(Integer position) throws ADTException;

    boolean containsKey(Integer position);

    void remove(Integer key) throws ADTException;

    Set<Integer> keySet();
}

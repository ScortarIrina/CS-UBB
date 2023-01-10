package Model.ADTs;

import Exceptions.ADTException;

import java.util.List;

public interface IStack<T> {
    T pop() throws ADTException;

    void push(T elem);

    boolean isEmpty();

    Object deepCopy();

    StringBuilder stackToString() throws ADTException;

    List<T> getReversed();
}

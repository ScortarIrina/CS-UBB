package Model.ADTs;

import Exceptions.ADTException;
import Model.Values.IValue;

import java.util.List;

public interface IList<T> {
    void add(T elem);
    T pop() throws ADTException;
    boolean isEmpty();

    T get(int pos);

    int length();

    String listToString();

    List<T> getList();
}

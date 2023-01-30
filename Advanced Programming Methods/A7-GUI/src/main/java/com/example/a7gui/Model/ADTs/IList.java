package com.example.a7gui.Model.ADTs;

import com.example.a7gui.Exceptions.InterpreterException;
import java.util.List;

public interface IList<T> {

    // adds an element to the list
    void add(T elem);

    // removes the first element from the list
    T pop() throws InterpreterException;

    // checks if the list is empty
    boolean isEmpty();

    // returns the element from a given position
    T get(int pos);

    // returns the length of the list
    int length();

    // converts the list to a string
    String listToString();

    // returns the list
    List<T> getList();
}

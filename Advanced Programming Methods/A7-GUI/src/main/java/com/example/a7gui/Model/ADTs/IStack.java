package com.example.a7gui.Model.ADTs;

import com.example.a7gui.Exceptions.InterpreterException;

import java.util.List;

public interface IStack<T> {

    // removes and returns the element from the top of the stack
    T pop() throws InterpreterException;

    // adds an element at the top of the stack
    void push(T elem);

    // checks if the stack is empty
    boolean isEmpty();

    Object deepCopy();

    // converts the stack to a string
    StringBuilder stackToString() throws InterpreterException;

    // returns the reversed stack
    List<T> getReversed();
}

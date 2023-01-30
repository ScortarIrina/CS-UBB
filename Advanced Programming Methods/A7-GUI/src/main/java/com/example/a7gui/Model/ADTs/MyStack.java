package com.example.a7gui.Model.ADTs;

import com.example.a7gui.Exceptions.InterpreterException;

import java.util.*;

public class MyStack<T> implements IStack<T> {

    Stack<T> stack;

    public MyStack() {
        this.stack  = new Stack<>();
    }

    @Override
    public T pop() throws InterpreterException {
        if(stack.isEmpty())
            throw new InterpreterException("ERROR: Stack is empty!");
        return this.stack.pop();
    }

    @Override
    public void push(T elem) {
        this.stack.push(elem);
    }

    @Override
    public boolean isEmpty() {
        return this.stack.isEmpty();
    }

    @Override
    public Object deepCopy() {
        Object copy = stack.clone();
        return copy;
    }

    public StringBuilder stackToString() throws InterpreterException {
        java.util.List<T> list = Arrays.asList((T[]) stack.toArray());
        Collections.reverse(list);
        StringBuilder str = new StringBuilder();
        //Object copy = deepCopy();
        for(T elem: list)
            str.append(elem.toString()+"\n");
        //str.append(copy.toString()+"\n");
        return str;
    }

    @Override
    public List<T> getReversed() {
        List<T> list = Arrays.asList((T[]) stack.toArray());
        Collections.reverse(list);
        return list;
    }
}


package com.example.a7gui.Model.ADTs;

import com.example.a7gui.Exceptions.InterpreterException;
import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements IList<T> {

    ArrayList<T> list;

    public MyList() {
        this.list = new ArrayList<>();
    }

    @Override
    public void add(T elem) {
        this.list.add(elem);
    }

    @Override
    public T pop() throws InterpreterException {
        if(list.isEmpty())
            throw new InterpreterException("ERROR: List is empty");
        return this.list.remove(0);
    }

    @Override
    public boolean isEmpty() {
        return this.list.isEmpty();
    }

    @Override
    public T get(int pos) {
        return list.get(pos);
    }

    @Override
    public int length() {
        return this.list.size();
    }

    @Override
    public List<T> getList() {
        return list;
    }

    public String listToString() {
        String string = "";
        for(int i = 0; i < length(); i++) {
            string = string + " " + get(i) + "\n";
        }
        return string;
    }
}


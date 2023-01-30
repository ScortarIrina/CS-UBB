package com.example.a7gui.Model.ProgramState;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.ADTs.IList;
import com.example.a7gui.Model.ADTs.IStack;
import com.example.a7gui.Model.Statements.IStatement;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Exceptions.InterpreterException;

import java.io.BufferedReader;
import java.util.List;

public class ProgramState {
    private IStack<IStatement> executionStack;
    private IDictionary<String, IValue> symbolTable;
    private IList<IValue> output;
    private IStatement originalProgram;
    private IDictionary<String, BufferedReader> fileTable;
    private IHeap heap;
    private int id;
    private static int lastID = 0;

    public ProgramState(IStack<IStatement> stack, IDictionary<String, IValue> symTable, IList<IValue> out,
                        IDictionary<String, BufferedReader> fileTable, IHeap heap, IStatement program) {
        this.executionStack = stack;
        this.symbolTable = symTable;
        this.output = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.originalProgram = program.deepCopy();
        this.executionStack.push(this.originalProgram);
        this.id = setID();
    }

    public ProgramState(IStack<IStatement> stack, IDictionary<String, IValue> symTable, IList<IValue> out,
                        IDictionary<String, BufferedReader> fileTable, IHeap heap) {
        this.executionStack = stack;
        this.symbolTable = symTable;
        this.output = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.id = setID();
    }

    public int getId() {
        return this.id;
    }

    public synchronized int setID() {
        lastID++;
        return lastID;
    }

    public void setExecutionStack(IStack<IStatement> newStack) {
        this.executionStack = newStack;
    }

    public void setSymbolTable(IDictionary<String, IValue> newSymTable) {
        this.symbolTable = newSymTable;
    }

    public void setOutput(IList<IValue> newOut) {
        this.output = newOut;
    }

    public void setFileTable(IDictionary<String, BufferedReader> fileTable) {
        this.fileTable = fileTable;
    }

    public void setHeap(IHeap newHeap) {
        this.heap = newHeap;
    }

    public IStack<IStatement> getExecutionStack() {
        return executionStack;
    }

    public IDictionary<String, IValue> getSymbolTable() {
        return symbolTable;
    }

    public IList<IValue> getOutput() {
        return output;
    }

    public IDictionary<String,BufferedReader> getFileTable() {
        return fileTable;
    }

    public IHeap getHeap() {
        return heap;
    }

    public boolean isNotCompleted() {
        return executionStack.isEmpty();
    }

    public ProgramState oneStep() throws InterpreterException {
        if (executionStack.isEmpty())
            throw new InterpreterException("ERROR: Program state stack is empty!");
        IStatement currentStatement = executionStack.pop();
        return currentStatement.execute(this);
    }

    public String executionStackToString() {
        StringBuilder executionStackStringBuilder = new StringBuilder();
        List<IStatement> stack = executionStack.getReversed();
        for (IStatement statement : stack) {
            executionStackStringBuilder.append(statement.toString()).append("\n");
        }
        return executionStackStringBuilder.toString();
    }

    public String symbolTableToString() throws InterpreterException {
        StringBuilder symbolTableStringBuilder = new StringBuilder();
        for (String key : symbolTable.getAllKeys()) {
            symbolTableStringBuilder.append(String.format("%s -> %s\n", key, symbolTable.search(key).toString()));
        }
        return symbolTableStringBuilder.toString();
    }

    public String outputToString() {
        StringBuilder outputStringBuilder = new StringBuilder();
        for (IValue elem : output.getList()) {
            outputStringBuilder.append(String.format("%s\n", elem.toString()));
        }
        return outputStringBuilder.toString();
    }

    public String fileTableToString() {
        StringBuilder fileTableStringBuilder = new StringBuilder();
        for (String key: fileTable.getAllKeys()) {
            fileTableStringBuilder.append(String.format("%s\n", key));
        }
        return fileTableStringBuilder.toString();
    }

    public String heapToString() throws InterpreterException {
        StringBuilder heapStringBuilder = new StringBuilder();
        for (int key : heap.keySet()) {
            heapStringBuilder.append(String.format("%d -> %s\n", key, heap.get(key)));
        }
        return heapStringBuilder.toString();
    }

    @Override
    public String toString() {
        return "Id: " + id + "\nExecution stack: \n" + executionStack.getReversed() + "\nSymbol table: \n" + symbolTable.toString() + "\nOutput list: \n" + output.toString() + "\nFile table:\n" + fileTable.toString() + "\nHeap memory:\n" + heap.toString() + "\n";
    }

    public String programStateToString() throws InterpreterException {
        return "Id: " + id + "\nExecution stack: \n" + executionStackToString() + "Symbol table: \n" + symbolTableToString() + "Output list: \n" + outputToString() + "File table:\n" + fileTableToString() + "Heap memory:\n" + heapToString();
    }
}


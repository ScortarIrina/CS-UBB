package Model.ProgramState;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.ADTs.IList;
import Model.ADTs.IStack;
import Model.Statements.IStatement;
import Model.Values.IValue;

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

    public ProgramState oneStep() throws StatementExecutionException, ADTException, ExpressionEvaluationException {
        if (executionStack.isEmpty())
            throw new StatementExecutionException("ERROR: Program state stack is empty!");
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

    public String symbolTableToString() throws ADTException {
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

    public String heapToString() throws ADTException {
        StringBuilder heapStringBuilder = new StringBuilder();
        for (int key : heap.keySet()) {
            heapStringBuilder.append(String.format("%d -> %s\n", key, heap.get(key)));
        }
        return heapStringBuilder.toString();
    }

    public String myToString() throws ADTException {
        return "ID: " + id +
                "\nExecution stack: \n" + executionStack.stackToString() +
                "\nSymbol table: \n" + symbolTable.dictToString() +
                "\nOutput list: \n" + output.listToString() +
                "\nFile table: \n" + fileTable.dictToString() +
                "\nHeap memory:\n" + heapToString() +
                "\n------------------------------------------------------------------------------------------------------------------------------------------------------";
    }

    public String programStateToString() throws ADTException {
        return "ID: " + id +
                "\nExecution stack: \n" + executionStackToString() +
                "\nSymbol table: \n" + symbolTableToString() +
                "\nOutput list: \n" + outputToString() +
                "\nFile table: \n" + fileTableToString() +
                "\nHeap memory:\n" + heapToString() +
                "\n------------------------------------------------------------------------------------------------------------------------------------------------------";
    }
}

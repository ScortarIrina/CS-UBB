package Controller;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IStack;
import Model.ProgramState.ProgramState;
import Model.Statements.IStatement;
import Model.Values.IValue;
import Model.Values.ReferenceValue;
import Repository.IRepository;

import java.io.IOException;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Controller {
    IRepository repository;
    boolean displayFlag = false;

    public Controller(IRepository repo) {
        this.repository = repo;
    }

    public void setDisplayFlag(boolean displayFlag) {
        this.displayFlag = displayFlag;
    }

    public Map<Integer, IValue> garbageCollector(List<Integer> symbolTableAddress, List<Integer> heapAddress, HashMap<Integer, IValue> heap) {
        return heap.entrySet().stream()
                .filter(e -> ( symbolTableAddress.contains(e.getKey()) || heapAddress.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public List<Integer> getAddressFromSymbolTable(Collection<IValue> symbolTable)
    {
        return symbolTable.stream().filter(value -> value instanceof ReferenceValue)
                .map(val -> {
                    ReferenceValue ref_value = (ReferenceValue) val;
                    return ref_value.getAddress();
                }).collect(Collectors.toList());
    }

    public ProgramState oneStep(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IStack<IStatement> stack = state.getExecutionStack();
        if(stack.isEmpty())
            throw new RuntimeException("ERROR: Program state stack is empty!");
        IStatement currentStatement = stack.pop();
        state.setExecutionStack(stack);
        return currentStatement.execute(state);
    }

    public void allSteps() throws StatementExecutionException, ExpressionEvaluationException, ADTException, IOException {
        ProgramState programState = repository.getCurrentState();
        this.repository.logProgramStateExecution();
        display();
        while(!programState.getExecutionStack().isEmpty()) {
            oneStep(programState);
            this.repository.logProgramStateExecution();
            display();

            // garbage collector
            programState.getHeap().setContent((HashMap<Integer, IValue>) garbageCollector(
                    getAddressFromSymbolTable(programState.getSymbolTable().getAll().values()),
                    programState.getHeap().keySet().stream().toList(), programState.getHeap().getContent()));

            this.repository.logProgramStateExecution();
        }
    }

    public void display() throws ADTException {
        if(displayFlag)
            System.out.println(this.repository.getCurrentState().myToString());
    }
}

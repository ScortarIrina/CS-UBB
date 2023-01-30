package com.example.a7gui.Controller;

import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.ReferenceValue;
import com.example.a7gui.Repository.IRepository;
import com.example.a7gui.Exceptions.InterpreterException;

import java.io.IOException;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Pair {
    final ProgramState first;
    final InterpreterException second;

    public Pair(ProgramState first, InterpreterException second) {
        this.first = first;
        this.second = second;
    }
}

public class Controller {

    IRepository repository;
    boolean displayFlag = false;
    ExecutorService executorService;

    public Controller(IRepository repo) {
        this.repository = repo;
    }

    public void setDisplayFlag(boolean displayFlag) {
        this.displayFlag = displayFlag;
    }

    public Map<Integer, IValue> safeGarbageCollector(List<Integer> symTableAddress, List<Integer> heapAddress, Map<Integer, IValue> heap) {
        return heap.entrySet().stream()
                .filter(e -> ( symTableAddress.contains(e.getKey()) || heapAddress.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public void conservativeGarbageCollector(List<ProgramState> programStates) {
        List<Integer> symTableAddresses = Objects.requireNonNull(programStates.stream()
                        .map(p -> getAddressFromSymTable(p.getSymbolTable().values()))
                        .map(Collection::stream)
                        .reduce(Stream::concat).orElse(null))
                .collect(Collectors.toList());
        programStates.forEach(p -> {
            p.getHeap().setContent((HashMap<Integer, IValue>) safeGarbageCollector(symTableAddresses, getAddressFromHeap(p.getHeap().getContent().values()), p.getHeap().getContent()));
        });
    }

    public List<Integer> getAddressFromSymTable(Collection<IValue> symTableValues) {
        return symTableValues.stream()
                .filter(v -> v instanceof ReferenceValue)
                .map(v -> {ReferenceValue v1 = (ReferenceValue) v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    public List<Integer> getAddressFromHeap(Collection<IValue> heapValues) {
        return heapValues.stream()
                .filter(v -> v instanceof ReferenceValue)
                .map(v -> {ReferenceValue v1 = (ReferenceValue) v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    public void oneStepForAllPrograms(List<ProgramState> programStates) throws InterruptedException, InterpreterException {
        programStates.forEach(programState -> {
            try {
                repository.logProgramStateExecution(programState);
                display(programState);
            } catch (IOException | InterpreterException e) {
                System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
            }
        });

        // prepare the list of callables
        List<Callable<ProgramState>> callList = programStates.stream()
                .map((ProgramState p) -> (Callable<ProgramState>) (p::oneStep))
                .collect(Collectors.toList());

        // start the execution of the callables
        // it returns the list of new created ProgramStates (namely threads)
        List<ProgramState> newProgramList = executorService.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (ExecutionException | InterruptedException e) {
                        System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
                    }
                    return null;
                })
                .filter(Objects::nonNull)
                .collect(Collectors.toList());

        // add the new created threads to the list of existing threads
        programStates.addAll(newProgramList);

        // after the execution, print the ProgramState List into the log file
        programStates.forEach(programState -> {
            try {
                repository.logProgramStateExecution(programState);
            } catch (IOException | InterpreterException e) {
                System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
            }
        });

        // save the current programs into the repository
        repository.setProgramStates(programStates);
    }

    public void oneStep() throws InterpreterException, InterruptedException {
        executorService = Executors.newFixedThreadPool(2);
        List<ProgramState> programStates = removeCompletedPrograms(repository.getProgramList());
        oneStepForAllPrograms(programStates);
        conservativeGarbageCollector(programStates);
        //programStates = removeCompletedPrg(repository.getProgramList());
        executorService.shutdownNow();
        //repository.setProgramStates(programStates);
    }

    public void allSteps() throws InterpreterException, InterruptedException {
        executorService = Executors.newFixedThreadPool(2);
        // remove the completed programs
        List<ProgramState> programStates = removeCompletedPrograms(repository.getProgramList());
        while (programStates.size() > 0) {
            conservativeGarbageCollector(programStates);
            oneStepForAllPrograms(programStates);
            // remove the completed programs
            programStates = removeCompletedPrograms(repository.getProgramList());
        }
        executorService.shutdownNow();
        // update the repository
        repository.setProgramStates(programStates);
    }

    private void display(ProgramState programState) {
        if (displayFlag) {
            System.out.println(programState.toString());
        }
    }

    public List<ProgramState> removeCompletedPrograms(List<ProgramState> inPrgList) {
        return inPrgList.stream()
                .filter(p -> !p.isNotCompleted())
                .collect(Collectors.toList());
    }

    public void setProgramStates(List<ProgramState> programStates) {
        this.repository.setProgramStates(programStates);
    }

    public List<ProgramState> getProgramStates() {
        return this.repository.getProgramList();
    }
}


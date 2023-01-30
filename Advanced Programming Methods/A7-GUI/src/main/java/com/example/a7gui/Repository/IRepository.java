package com.example.a7gui.Repository;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ProgramState.ProgramState;

import java.io.IOException;
import java.util.List;

public interface IRepository {

    List<ProgramState> getProgramList();

    void setProgramStates(List<ProgramState> programStates);

    void addProgram(ProgramState program);

    void logProgramStateExecution(ProgramState programState) throws IOException, InterpreterException;

    void emptyLogFile() throws IOException;
}

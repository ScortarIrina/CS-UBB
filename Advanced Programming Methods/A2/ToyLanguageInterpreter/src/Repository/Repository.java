package Repository;
import Exceptions.ADTException;
import Model.ProgramState.ProgramState;
import Model.ADTs.*;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepository {
    private List<ProgramState> programStates;
    private int currentPosition;
    private String logFilePath;

    public Repository(ProgramState programState, String logFilePath) {
        this.logFilePath = logFilePath;
        this.programStates = new ArrayList<>();
        this.currentPosition = 0;
        addProgram(programState);
//        emptyLogFile();
    }

    public int getCurrentPosition() {
        return currentPosition;
    }

    public void setCurrentPosition(int currentPosition) {
        this.currentPosition = currentPosition;
    }

    @Override
    public List<ProgramState> getProgramList() {
        return this.programStates;
    }

    @Override
    public void setProgramStates(List<ProgramState> programStates) {
        this.programStates = programStates;
    }


    @Override
    public void addProgram(ProgramState program) {
        this.programStates.add(program);
    }

    @Override
    public ProgramState getCurrentState() {
        return this.programStates.get(this.currentPosition);
    }

    @Override
    public void logProgramStateExecution() throws IOException, ADTException {
        PrintWriter logFile;
        logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath,true)));
        logFile.println(this.programStates.get(0).myToString());
        logFile.close();
    }

    @Override
    public void emptyLogFile() throws IOException {
        PrintWriter logFile;
        logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, false)));
        logFile.close();
    }
}

package Repository;
import Exceptions.ADTException;
import Model.ProgramState.ProgramState;

import java.io.IOException;
import java.util.List;

public interface IRepository {

    List<ProgramState> getProgramList();

    void setProgramStates(List<ProgramState> programStates);

    void addProgram(ProgramState program);

    void logProgramStateExecution(ProgramState programState) throws IOException, ADTException;

    void emptyLogFile() throws IOException;
}

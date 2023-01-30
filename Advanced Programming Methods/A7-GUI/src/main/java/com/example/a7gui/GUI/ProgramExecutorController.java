package com.example.a7gui.GUI;

import com.example.a7gui.Controller.Controller;
import com.example.a7gui.Exceptions.*;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Statements.IStatement;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Values.IValue;

import java.util.*;
import java.util.stream.Collectors;

class Pair<T1, T2> {
    T1 first;
    T2 second;

    public Pair(T1 first, T2 second) {
        this.first = first;
        this.second = second;
    }
}

public class ProgramExecutorController {

    private Controller controller;

    @FXML
    private TextField numberProgramStatesField;
    @FXML
    private TableView<Pair<Integer, IValue>> heapTableView;
    @FXML
    private TableColumn<Pair<Integer, IValue>, Integer> addressColumn;
    @FXML
    private TableColumn<Pair<Integer, IValue>, String> valueColumn;
    @FXML
    private ListView<String> outputListView;
    @FXML
    private ListView<String> fileTableListView;
    @FXML
    private ListView<Integer> programStateIDsListView;
    @FXML
    private TableView<Pair<String, IValue>> symbolTableView;
    @FXML
    private TableColumn<Pair<String, IValue>, String> variableNameColumn;
    @FXML
    private TableColumn<Pair<String, IValue>, String> variableValueColumn;
    @FXML
    private ListView<String> executionStackListView;
    @FXML
    private Button runOneStepButton;

    public void setController(Controller controller) {
        this.controller = controller;
        populate();
    }

    @FXML
    public void initialize() {
        programStateIDsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
        addressColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().first).asObject());
        valueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));
        variableNameColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().first));
        variableValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));
    }

    private void populate() {
        populateHeapTableView();
        populateOutputListView();
        populateFileTableListView();
        populateProgramStateIDsListView();
        populateSymbolTableView();
        populateExecutionStackListView();

    }

    private void populateExecutionStackListView() {
        ProgramState programState = getCurrentProgramState();
        List<String> executionStackToString = new ArrayList<>();
        if (programState != null)
            for (IStatement statement: programState.getExecutionStack().getReversed()) {
                executionStackToString.add(statement.toString());
            }
        executionStackListView.setItems(FXCollections.observableList(executionStackToString));
    }

    private void populateSymbolTableView() {
        ProgramState programState = getCurrentProgramState();
        IDictionary<String, IValue> symbolTable = Objects.requireNonNull(programState).getSymbolTable();
        ArrayList<Pair<String, IValue>> symbolTableEntries = new ArrayList<>();
        for (Map.Entry<String, IValue> entry: symbolTable.getContent().entrySet()) {
            symbolTableEntries.add(new Pair<>(entry.getKey(), entry.getValue()));
        }
        symbolTableView.setItems(FXCollections.observableArrayList(symbolTableEntries));
    }

    private void populateProgramStateIDsListView() {
        List<ProgramState> programStates = controller.getProgramStates();
        List<Integer> idList = programStates.stream().map(ProgramState::getId).collect(Collectors.toList());
        programStateIDsListView.setItems(FXCollections.observableList(idList));
        populateNumberOfProgramStatesTextField();
    }

    private void populateFileTableListView() {
        ProgramState programState = getCurrentProgramState();
        List<String> files = new ArrayList<>(Objects.requireNonNull(programState).getFileTable().getContent().keySet());
        fileTableListView.setItems(FXCollections.observableList(files));
    }

    private void populateOutputListView() {
        ProgramState programState = getCurrentProgramState();
        List<String> output = new ArrayList<>();
        List<IValue> outputList = Objects.requireNonNull(programState).getOutput().getList();
        for (int index = 0; index < outputList.size(); index++) {
            output.add(outputList.get(index).toString());
        }
        outputListView.setItems(FXCollections.observableArrayList(output));
    }

    private void populateHeapTableView() {
        ProgramState programState = getCurrentProgramState();
        IHeap heap = Objects.requireNonNull(programState).getHeap();
        ArrayList<Pair<Integer, IValue>> heapEntries = new ArrayList<>();
        for (Map.Entry<Integer, IValue> entry : heap.getContent().entrySet()) {
            heapEntries.add(new Pair<>(entry.getKey(), entry.getValue()));
        }
        heapTableView.setItems(FXCollections.observableArrayList(heapEntries));
    }

    @FXML
    private void changeProgramState(MouseEvent event) {
        populateExecutionStackListView();
        populateSymbolTableView();
    }

    private ProgramState getCurrentProgramState() {
        if (controller.getProgramStates().size() == 0)
            return null;
        else {
            int currentId = programStateIDsListView.getSelectionModel().getSelectedIndex();
            if (currentId == -1)
                return controller.getProgramStates().get(0);
            else
                return controller.getProgramStates().get(currentId);
        }
    }

    private void populateNumberOfProgramStatesTextField() {
        List<ProgramState> programStates = controller.getProgramStates();
        numberProgramStatesField.setText(String.valueOf(programStates.size()));
    }

    @FXML
    private void runOneStep(MouseEvent mouseEvent) {
        if (controller != null) {
            try {
                List<ProgramState> programStates = Objects.requireNonNull(controller.getProgramStates());
                if (programStates.size() > 0) {
                    controller.oneStep();
                    populate();
                    programStates = controller.removeCompletedPrograms(controller.getProgramStates());
                    controller.setProgramStates(programStates);
                    populateProgramStateIDsListView();
                } else {
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Error!");
//                    alert.setHeaderText("An error has occurred!");
                    alert.setContentText("There is nothing left to execute!");
                    alert.showAndWait();
                }
            } catch (InterpreterException | InterruptedException e) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Execution error!");
//                alert.setHeaderText("An execution error has occurred!");
                alert.setContentText(e.getMessage());
                alert.showAndWait();
            }
        } else {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error!");
//            alert.setHeaderText("An error has occurred!");
            alert.setContentText("No program selected!");
            alert.showAndWait();
        }
    }
}

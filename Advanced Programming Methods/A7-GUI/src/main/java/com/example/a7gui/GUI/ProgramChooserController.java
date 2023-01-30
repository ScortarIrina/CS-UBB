package com.example.a7gui.GUI;

import com.example.a7gui.Controller.Controller;
import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.MyDictionary;
import com.example.a7gui.Model.ADTs.MyHeap;
import com.example.a7gui.Model.ADTs.MyList;
import com.example.a7gui.Model.ADTs.MyStack;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Statements.IStatement;
import com.example.a7gui.Model.Statements.CompoundStatement;
import com.example.a7gui.Model.Statements.AssignmentStatement;
import com.example.a7gui.Model.Statements.CloseReadFile;
import com.example.a7gui.Model.Statements.ForkStatement;
import com.example.a7gui.Model.Statements.IfStatement;
import com.example.a7gui.Model.Statements.NewStatement;
import com.example.a7gui.Model.Statements.OpenReadFile;
import com.example.a7gui.Model.Statements.PrintStatement;
import com.example.a7gui.Model.Statements.ReadFile;
import com.example.a7gui.Model.Statements.VariableDeclarationStatement;
import com.example.a7gui.Model.Statements.WhileStatement;
import com.example.a7gui.Model.Statements.WriteHeapStatement;
import com.example.a7gui.Repository.IRepository;
import com.example.a7gui.Repository.Repository;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import com.example.a7gui.Model.Expressions.ArithmeticExpression;
import com.example.a7gui.Model.Expressions.ReadHeapExpression;
import com.example.a7gui.Model.Expressions.RelationalExpression;
import com.example.a7gui.Model.Expressions.ValueExpression;
import com.example.a7gui.Model.Expressions.VariableExpression;
import com.example.a7gui.Model.Types.IntType;
import com.example.a7gui.Model.Types.BoolType;
import com.example.a7gui.Model.Types.ReferenceType;
import com.example.a7gui.Model.Types.StringType;
import com.example.a7gui.Model.Values.BoolValue;
import com.example.a7gui.Model.Values.IntValue;
import com.example.a7gui.Model.Values.StringValue;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ProgramChooserController {

    private ProgramExecutorController programExecutorController;

    public void setProgramExecutorController(ProgramExecutorController programExecutorController) {
        this.programExecutorController = programExecutorController;
    }

    @FXML
    private ListView<IStatement> programsListView;

    @FXML
    private Button displayButton;

    @FXML
    public void initialize() {
        programsListView.setItems(getAllStatements());
        programsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
    }

    @FXML
    private void displayProgram(ActionEvent actionEvent) {
        IStatement selectedStatement = programsListView.getSelectionModel().getSelectedItem();
        if (selectedStatement == null) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error encountered!");
            alert.setContentText("No statement selected!");
            alert.showAndWait();
        } else {
            int id = programsListView.getSelectionModel().getSelectedIndex();
            try {
                selectedStatement.typeCheck(new MyDictionary<>());
                ProgramState programState = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), selectedStatement);
                IRepository repository = new Repository(programState, "log" + (id + 1) + ".txt");
                Controller controller = new Controller(repository);
                programExecutorController.setController(controller);
            } catch (InterpreterException | IOException exception) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Error encountered!");
                alert.setContentText(exception.getMessage());
                alert.showAndWait();
            }
        }
    }

    @FXML
    private ObservableList<IStatement> getAllStatements() {
        List<IStatement> allStatements = new ArrayList<>();

        IStatement ex1 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));
        allStatements.add(ex1);

        IStatement ex2 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ArithmeticExpression(new ValueExpression(new IntValue(2)),'+', new
                                ArithmeticExpression(new ValueExpression(new IntValue(3)), '*', new ValueExpression(new IntValue(5))))),
                                new CompoundStatement(new AssignmentStatement("b",new ArithmeticExpression(new VariableExpression("a"), '+', new ValueExpression(new
                                        IntValue(1)))), new PrintStatement(new VariableExpression("b"))))));
        allStatements.add(ex2);

        IStatement ex3 = new CompoundStatement(new VariableDeclarationStatement("a", new BoolType()),
                new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ValueExpression(new BoolValue(true))),
                                new CompoundStatement(new IfStatement(new VariableExpression("a"),
                                        new AssignmentStatement("v", new ValueExpression(new IntValue(2))),
                                        new AssignmentStatement("v", new ValueExpression(new IntValue(3)))),
                                        new PrintStatement(new VariableExpression("v"))))));
        allStatements.add(ex3);

        IStatement ex4 = new CompoundStatement(new VariableDeclarationStatement("varf", new StringType()),
                new CompoundStatement(new AssignmentStatement("varf", new ValueExpression(new StringValue("test.in"))),
                        new CompoundStatement(new OpenReadFile(new VariableExpression("varf")),
                                new CompoundStatement(new VariableDeclarationStatement("varc", new IntType()),
                                        new CompoundStatement(new ReadFile(new VariableExpression("varf"), "varc"),
                                                new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                                        new CompoundStatement(new ReadFile(new VariableExpression("varf"), "varc"),
                                                                new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                                                        new CloseReadFile(new VariableExpression("varf"))))))))));
        allStatements.add(ex4);

        IStatement ex5 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ValueExpression(new IntValue(5))),
                                new CompoundStatement(new AssignmentStatement("b", new ValueExpression(new IntValue(7))),
                                        new IfStatement(new RelationalExpression(new VariableExpression("a"), ">", new VariableExpression("b")),new PrintStatement(new VariableExpression("a")),
                                                new PrintStatement(new VariableExpression("b")))))));
        allStatements.add(ex5);

        IStatement ex6 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(4))),
                        new CompoundStatement(new WhileStatement(new RelationalExpression(new VariableExpression("v"), ">", new ValueExpression(new IntValue(0))),
                                new CompoundStatement(new PrintStatement(new VariableExpression("v")), new AssignmentStatement("v",new ArithmeticExpression(new VariableExpression("v"), '-', new ValueExpression(new IntValue(1)))))),
                                new PrintStatement(new VariableExpression("v")))));
        allStatements.add(ex6);

        IStatement ex7 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new VariableExpression("a")))))));
        allStatements.add(ex7);

        IStatement ex8 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))),
                                                new PrintStatement(new ArithmeticExpression(new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a"))), '+',new ValueExpression(new IntValue(5)))))))));
        allStatements.add(ex8);

        IStatement ex9 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement( new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))),
                                new CompoundStatement(new WriteHeapStatement("v", new ValueExpression(new IntValue(30))),
                                        new PrintStatement(new ArithmeticExpression(new ReadHeapExpression(new VariableExpression("v")), '+', new ValueExpression(new IntValue(5))))))));
        allStatements.add(ex9);

        IStatement ex10 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(30))),
                                                new PrintStatement(new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a")))))))));
        allStatements.add(ex10);

        IStatement ex11 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new IntType())),
                        new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(10))),
                                new CompoundStatement(new NewStatement("a", new ValueExpression(new IntValue(22))),
                                        new CompoundStatement(new ForkStatement(new CompoundStatement(new WriteHeapStatement("a", new ValueExpression(new IntValue(30))),
                                                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(32))),
                                                        new CompoundStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new ReadHeapExpression(new VariableExpression("a"))))))),
                                                new CompoundStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new ReadHeapExpression(new VariableExpression("a")))))))));
        allStatements.add(ex11);
        return FXCollections.observableArrayList(allStatements);
    }
}

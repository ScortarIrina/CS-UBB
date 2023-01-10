package View;

import Controller.Controller;
import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.*;
import Model.Expressions.ArithmeticExpression;
import Model.Expressions.ValueExpression;
import Model.Expressions.VariableExpression;
import Model.ProgramState.ProgramState;
import Model.Statements.*;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Values.BoolValue;
import Model.Values.IValue;
import Model.Values.IntValue;
import Repository.IRepository;
import Repository.Repository;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

public class View {
    public void displayMenu() {
        System.out.println("MENU: ");
        System.out.println("0. Exit.");
        System.out.println("1. Run the first program: \n\tint v;\n\tv=2;\n\tPrint(v)");
        System.out.println("2. Run the second program: \n\tint a;\n\tint b;\n\ta=2+3*5;\n\tb=a+1;\n\tPrint(b)");
        System.out.println("3. Run the third program: \n\tbool a;\n\tint v;\n\ta=true;\n\t(If a Then v=2 Else v=3);\n\tPrint(v)");
        System.out.println("Choose an option: ");
    }

    private void runProgram1() throws StatementExecutionException, ExpressionEvaluationException, ADTException, IOException {
        IStatement p1 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));
        runStatement(p1);
    }

    private void runProgram2() throws StatementExecutionException, ExpressionEvaluationException, ADTException, IOException {
        IStatement p2 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ArithmeticExpression(new ValueExpression(new IntValue(2)), '+',
                                new ArithmeticExpression(new ValueExpression(new IntValue(3)), '*', new ValueExpression(new IntValue(5))))),
                                new CompoundStatement(new AssignmentStatement("b", new ArithmeticExpression(new VariableExpression("a"), '+', new ValueExpression(new IntValue(1)))),
                                        new PrintStatement(new VariableExpression("b"))))));
        runStatement(p2);
    }

    private void runProgram3() throws StatementExecutionException, ExpressionEvaluationException, ADTException, IOException {
        IStatement p3 = new CompoundStatement((new VariableDeclarationStatement("a", new BoolType())),
                new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ValueExpression(new BoolValue(true))),
                                new CompoundStatement(new IfStatement(new VariableExpression("a"), new AssignmentStatement("v", new ValueExpression(new IntValue(2))),
                                        new AssignmentStatement("v", new ValueExpression(new IntValue(3)))), new PrintStatement(new VariableExpression("v"))))));

        runStatement(p3);
    }


    private void runStatement(IStatement statement) throws StatementExecutionException, ExpressionEvaluationException, ADTException, IOException {
        IStack<IStatement> executionStack = new MyStack<>();
        IDictionary<String, IValue> symbolTable = new MyDictionary<>();
        IList<IValue> output = new MyList<>();
        IDictionary<String, BufferedReader> fileTable = new MyDictionary<>();
        IHeap heap = new MyHeap();

        ProgramState state = new ProgramState(executionStack, symbolTable, output, fileTable, heap, statement);

        IRepository repo = new Repository(state, "log.txt");
        Controller ctrl = new Controller(repo);

        System.out.println("Do you want to display the steps?[yes/no]");
        Scanner s = new Scanner(System.in);
        String option = s.next();
        ctrl.setDisplayFlag(Objects.equals(option, "yes"));
        ctrl.allSteps();
        System.out.println("Result is" + state.getOutput().toString().replace('[', ' ').replace(']', ' '));
    }

    public void start() {
        boolean running = true;

        while (running) {

            try {
                displayMenu();
                System.out.println("Choose an option: ");
                Scanner s = new Scanner(System.in);
                int opt = s.nextInt();
                int prgNo;
                if (opt == 0) {
                    running = false;
                }
                else if (opt == 1) {
                    System.out.println("Which program would you like to input?");
                    System.out.println("1. int v; v=2; Print(v)");
                    System.out.println("2. int a; int b; a=2+3*5; b=a+1; Print(b)");
                    System.out.println("3. bool a; int v; a=true; (If a Then v=2 Else v=3); Print(v)");
                    Scanner s2 = new Scanner(System.in);
                    prgNo = s2.nextInt();
                    if (prgNo == 1) {
                        runProgram1();
                    }
                    else if (prgNo == 2) {
                        runProgram2();
                    }
                    else if (prgNo == 3) {
                        runProgram3();
                    }
                }
            }
            catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
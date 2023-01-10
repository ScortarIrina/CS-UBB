package View;

import Controller.Controller;
import Model.ADTs.MyDictionary;
import Model.ADTs.MyHeap;
import Model.ADTs.MyList;
import Model.ADTs.MyStack;
import Model.Expressions.*;
import Model.ProgramState.ProgramState;
import Model.Statements.*;
import Model.Types.IntType;
import Model.Types.ReferenceType;
import Model.Types.StringType;
import Model.Values.IValue;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Repository.IRepository;
import Repository.Repository;

import java.io.BufferedReader;


public class Interpreter {
    public static void main(String[] args) {

        IStatement ex1 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
            new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(2))),
                    new PrintStatement(new VariableExpression("v"))));

        ProgramState prg1 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex1);
        IRepository repo1 = new Repository(prg1, "log1.txt");
        Controller ctrl1 = new Controller(repo1);



        IStatement ex2 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ArithmeticExpression(new ValueExpression(new IntValue(2)), '+',
                                new ArithmeticExpression(new ValueExpression(new IntValue(3)), '*', new ValueExpression(new IntValue(5))))),
                                new CompoundStatement(new AssignmentStatement("b", new ArithmeticExpression(new VariableExpression("a"), '+', new ValueExpression(new IntValue(1)))),
                                        new PrintStatement(new VariableExpression("b"))))));

        ProgramState prg2 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex2);
        IRepository repo2 = new Repository(prg2, "log2.txt");
        Controller ctrl2 = new Controller(repo2);



        IStatement ex3 = new CompoundStatement((new VariableDeclarationStatement("a", new IntType())),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ValueExpression(new IntValue(2))),
                            new CompoundStatement(new AssignmentStatement("b", new ValueExpression(new IntValue(20))),
                                new CompoundStatement(new IfStatement(new RelationalExpression(new VariableExpression("a"), "<", new VariableExpression("b")), new AssignmentStatement("a", new ValueExpression(new IntValue(200))),
                                        new AssignmentStatement("v", new ValueExpression(new IntValue(3)))), new PrintStatement(new VariableExpression("a")))))));

        ProgramState prg3 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex3);
        IRepository repo3 = new Repository(prg3, "log3.txt");
        Controller ctrl3 = new Controller(repo3);



        IStatement ex4 = new CompoundStatement(new VariableDeclarationStatement("varf", new StringType()),
                new CompoundStatement(new AssignmentStatement("varf", new ValueExpression(new StringValue("test.in"))),
                        new CompoundStatement(new OpenReadFile(new VariableExpression("varf")),
                                new CompoundStatement(new VariableDeclarationStatement("varc", new IntType()),
                                        new CompoundStatement(new ReadFile(new VariableExpression("varf"), "varc"),
                                                new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                                        new CompoundStatement(new ReadFile(new VariableExpression("varf"), "varc"),
                                                                new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                                                        new CloseReadFile(new VariableExpression("varf"))))))))));

        ProgramState prg4 = new ProgramState(new MyStack<>(),new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex4);
        IRepository repo4 = new Repository(prg4, "log4.txt");
        Controller ctrl4 = new Controller(repo4);



        IStatement ex5 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignmentStatement("a", new ValueExpression(new IntValue(5))),
                                new CompoundStatement(new AssignmentStatement("b", new ValueExpression(new IntValue(7))),
                                        new IfStatement(new RelationalExpression(new VariableExpression("a"), ">",
                                                new VariableExpression("b")),new PrintStatement(new VariableExpression("a")),
                                                new PrintStatement(new VariableExpression("b")))))));

        ProgramState prg5 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex5);
        IRepository repo5 = new Repository(prg5, "log5.txt");
        Controller ctrl5 = new Controller(repo5);



        IStatement ex6 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(4))),
                        new CompoundStatement(new WhileStatement(new RelationalExpression(new VariableExpression("v"), ">", new ValueExpression(new IntValue(0))),
                                new CompoundStatement(new PrintStatement(new VariableExpression("v")), new AssignmentStatement("v", new ArithmeticExpression(new VariableExpression("v"), '-', new ValueExpression(new IntValue(1)))))),
                                new PrintStatement(new VariableExpression("v")))));

        ProgramState prg6 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex6);
        IRepository repo6 = new Repository(prg6, "log6.txt");
        Controller ctrl6 = new Controller(repo6);



        IStatement ex7 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new VariableExpression("a")))))));

        ProgramState prg7 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex7);
        IRepository repo7 = new Repository(prg7, "log7.txt");
        Controller ctrl7 = new Controller(repo7);



        IStatement ex8 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                                new CompoundStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(30))),
                                                new PrintStatement(new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a")))))))));

        ProgramState prg8 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex8);
        IRepository repo8 = new Repository(prg8, "log8.txt");
        Controller ctrl8 = new Controller(repo8);



        IStatement ex9 = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new NewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement( new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))),
                                new CompoundStatement(new WriteHeapStatement("v", new ValueExpression(new IntValue(30))),
                                        new PrintStatement(new ArithmeticExpression(new ReadHeapExpression(new VariableExpression("v")), '+', new ValueExpression(new IntValue(5))))))));

        ProgramState prg9 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex9);
        IRepository repo9 = new Repository(prg9, "log9.txt");
        Controller ctrl9 = new Controller(repo9);



        IStatement ex10 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignmentStatement("v", new ValueExpression(new IntValue(4))),
                        new CompoundStatement(new WhileStatement(new RelationalExpression(new VariableExpression("v"), ">", new ValueExpression(new IntValue(0))),
                                new CompoundStatement(new PrintStatement(new VariableExpression("v")), new AssignmentStatement("v", new ArithmeticExpression(new VariableExpression("v"), '-', new ValueExpression(new IntValue(1)))))), new PrintStatement(new VariableExpression("v")))));

        ProgramState prg10 = new ProgramState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap(), ex10);
        IRepository repo10 = new Repository(prg10, "log10.txt");
        Controller ctrl10 = new Controller(repo10);


        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunCommand("1", ex1.toString(), ctrl1));
        menu.addCommand(new RunCommand("2", ex2.toString(), ctrl2));
        menu.addCommand(new RunCommand("3", ex3.toString(), ctrl3));
        menu.addCommand(new RunCommand("4", ex4.toString(), ctrl4));
        menu.addCommand(new RunCommand("5", ex5.toString(), ctrl5));
        menu.addCommand(new RunCommand("6", ex6.toString(), ctrl6));
        menu.addCommand(new RunCommand("7", ex7.toString(), ctrl7));
        menu.addCommand(new RunCommand("8", ex8.toString(), ctrl8));
        menu.addCommand(new RunCommand("9", ex9.toString(), ctrl9));
        menu.addCommand(new RunCommand("10", ex10.toString(), ctrl10));
        menu.show();

    }
}

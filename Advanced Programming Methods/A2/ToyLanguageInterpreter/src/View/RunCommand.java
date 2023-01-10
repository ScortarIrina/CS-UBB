package View;

import Controller.Controller;
import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

public class RunCommand extends Command {
    private Controller controller;

    public RunCommand(String key, String description1, Controller ctrl) {
        super(key,description1);
        this.controller = ctrl;
    }

    @Override
    public void execute() {
        try {
            System.out.println("Do you want to display the steps?");
            Scanner readOption = new Scanner(System.in);
            String opt = readOption.next();
            controller.setDisplayFlag(Objects.equals(opt, "yes") || Objects.equals(opt, "Yes") || Objects.equals(opt, "Y") || Objects.equals(opt, "y"));
            controller.allSteps();
        }
        catch(ExpressionEvaluationException | ADTException | StatementExecutionException | IOException e) {
            System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
        }
    }
}

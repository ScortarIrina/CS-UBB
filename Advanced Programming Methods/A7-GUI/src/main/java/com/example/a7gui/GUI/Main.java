package com.example.a7gui.GUI;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.util.Objects;

public class Main extends Application  {

    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader programListLoader = new FXMLLoader();
        programListLoader.setLocation(this.getClass().getClassLoader().getResource("ProgramChooserController.fxml"));
        Parent programListRoot = programListLoader.load();
        Scene programListScene = new Scene(programListRoot, 900, 500);
        programListScene.getStylesheets().add(Objects.requireNonNull(this.getClass().getClassLoader().getResource("button_style.css")).toExternalForm());
        ProgramChooserController programChooserController = programListLoader.getController();
        primaryStage.setTitle("Select a program");
        primaryStage.setScene(programListScene);
        primaryStage.show();

        FXMLLoader programExecutorLoader = new FXMLLoader();
        programExecutorLoader.setLocation(this.getClass().getClassLoader().getResource("ProgramExecutorController.fxml"));
        Parent programExecutorRoot = programExecutorLoader.load();
        Scene programExecutorScene = new Scene(programExecutorRoot, 700, 500);
        programExecutorScene.getStylesheets().add(Objects.requireNonNull(this.getClass().getClassLoader().getResource("button_style.css")).toExternalForm());
        ProgramExecutorController programExecutorController = programExecutorLoader.getController();
        programChooserController.setProgramExecutorController(programExecutorController);
        Stage secondaryStage = new Stage();
        secondaryStage.setTitle("Toy Language Interpreter");
        secondaryStage.setScene(programExecutorScene);
        secondaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

}

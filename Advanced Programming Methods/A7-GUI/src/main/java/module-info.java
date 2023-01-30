module com.example.a7gui {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.example.a7gui to javafx.fxml;
    opens com.example.a7gui.GUI to javafx.graphics, javafx.fxml;
    exports com.example.a7gui;
}
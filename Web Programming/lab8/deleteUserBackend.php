<?php

// import the file with the DB configuration
require_once "utils/configuration.php";

// variable to connect to the DB
global $connection;

// check if the id field in the $_POST array is set and not empty
if (isset($_POST['id']) && !empty(trim($_POST['id']))) {

    // assign it to a variable
    $id = $_POST['id'];

    // construct sql query for deletion
    $sql_query = "delete from User where userID = '$id';";

    // execute the query
    $result = mysqli_query($connection, $sql_query);

    // check if the result of the query was successful
    if ($result) {
        echo "Your user was deleted successfully!";
        header("Location: showUsers.html");
    } else {
        echo "Oops! Something went wrong and your user cannot be deleted! Please try again later.";
    }
}

// close the connection
mysqli_close($connection);
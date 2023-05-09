<?php

// include the file that defines the database connection variables
require_once "utils/configuration.php";

// retrieve the data from the $_POST super global array
$name = $_POST['name'];
$username = $_POST['username'];
$password = $_POST['password'];
$age = $_POST['age'];
$role = $_POST['role'];
$email = $_POST['email'];
$webpage = $_POST['webpage'];

// build a sql query for inserting the data into the database
$sql_query = "insert into User(name, username, password, age, role, email, webpage) 
values ('$name', '$username', '$password', $age, '$role', '$email', '$webpage')";

// use the global keyword to access the database connection variable defined in the configuration.php file
global $connection;

// execute the query
$result = mysqli_query($connection, $sql_query);

// check if the result of the query was successful
if ($result) {
    echo "Your user was added successfully!";
    // redirect the user to the showUsers.html page
    header("Location: showUsers.html");
} else {
    echo "Oops!Something went wrong and your document cannot be added!Please try again later.";
}

// close the database connection
mysqli_close($connection);
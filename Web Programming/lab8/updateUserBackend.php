<?php

// import configuration file of the database
require_once "utils/configuration.php";

// retrieve form data from the $_POST super global array
$userID = $_POST['id'];
$name = $_POST['name'];
$username = $_POST['username'];
$password = $_POST['password'];
$age = $_POST['age'];
$role = $_POST['role'];
$email = $_POST['email'];
$webpage = $_POST['webpage'];

// create a query for updating the user using the retrieved data from the form
$sql_query = "update User 
              set name='$name', username = '$username', password = '$password', age = $age, role = '$role', 
                  email = '$email', webpage = '$webpage' 
              where userID = $userID";

// define the connection
global $connection;

// execute the query
$result = mysqli_query($connection, $sql_query);

// check if the result is correct
if ($result) {
    echo "Your user was updated successfully!";
    header("Location: showUsers.html");
} else {
    echo "Oops!Something went wrong and your document cannot be added!Please try again later.";
}

// close DB connection
mysqli_close($connection);

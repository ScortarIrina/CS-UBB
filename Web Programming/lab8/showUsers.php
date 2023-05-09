<?php

// import the configuration file for the DB
require_once 'utils/configuration.php';

// define a connection to the DB
global $connection;

// construct a new query
$sql_query = "SELECT * FROM User;";

// execute the created query
$result = mysqli_query($connection, $sql_query);

// if the result is not null
if ($result) {

    // get the number of rows returned by the query
    $number_of_rows = mysqli_num_rows($result);

    // initialize an array to store the requested users
    $requested_users = array();

    // get the values of the role and name parameters passed through the GET request
    $role = $_GET["role"];
    $name = $_GET["name"];

    // loop through each row o the result
    for ($i = 0; $i < $number_of_rows; $i++) {
        $row = mysqli_fetch_array($result);

        // check if the role and name match the requested parameters
        if (str_contains($row["role"], $role) && str_contains($row["name"], $name))
            // if the row matches the requested parameters, add it to the requested_users array
            $requested_users[] = array($row['userID'], $row['name'], $row['username'], $row['age'], $row['role'], $row['email'], $row['webpage']);
    }

    // free the memory
    mysqli_free_result($result);

    // encode the requested_users as JSOn and give them as an output
    echo json_encode($requested_users);
}

// close the DB connection
mysqli_close($connection);
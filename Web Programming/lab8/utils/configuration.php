<?php

// define the server name, username, password and database for the MySql DB
$dbServerName = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "Enterprise";

// establish the connection to the DB using the credentials above
$connection = mysqli_connect($dbServerName, $dbUsername, $dbPassword, $dbName);

// check if the connection was successful
if ($connection === false) {
    die("ERROR: Could not connect." . mysqli_connect_error());
}
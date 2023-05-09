<?php
require_once "utils/configuration.php";
global $connection;
$id = "";
$name = "";
$username = "";
$password = "";
$age = "";
$role = "";
$email = "";
$webpage = "";
if (isset($_GET['id']) && !empty(trim($_GET['id']))) {
    $id = trim($_GET['id']);
    $sql_query = "select * from user where userID = $id;";
    $result = mysqli_query($connection, $sql_query);
    if ($result) {
        $number_of_rows = mysqli_num_rows($result);
        if ($number_of_rows == 1) {
            $row = mysqli_fetch_array($result);
            $name = $row['name'];
            $username = $row['username'];
            $password = $row['password'];
            $age = $row['age'];
            $role = $row['role'];
            $email = $row['email'];
            $webpage = $row['webpage'];
        } else {
            die("Incorrect user id");
        }
    } else {
        die("Oops! Something went wrong and your document cannot be updated! Please try again later.");
    }
    mysqli_close($connection);
} else die("Oops! Something went wrong and your document cannot be updated! Please try again later.");
?>

<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Update User</title>
    <style>
        <?php include "addUser.css" ?>
    </style>
</head>

<body>
<div class="container">
    <h1>Update User</h1>
    <p><b>Please fill this form and submit to update the user in the database.</b></p>

    <!--  form for updating a user  -->
    <form action="updateUserBackend.php" method="post">
        <!--  input fields for updating the user  -->
        <input type="hidden" name="id" value="<?php echo trim($_GET['id']); ?>">
        <label>
            <input type="text" name="name" placeholder="Name:" value="<?php echo $name ?>">
        </label> <br>
        <label>
            <input type="text" name="username" placeholder="Username:" value="<?php echo $username ?>">
        </label> <br>
        <label>
            <input type="password" name="password" placeholder="Password:" value="<?php echo $password ?>">
        </label> <br>
        <label>
            <input type="number" name="age" placeholder="Age:" value="<?php echo $age ?>">
        </label> <br>
        <label>
            <input type="text" name="role" placeholder="Role:" value="<?php echo $role ?>">
        </label> <br>
        <label>
            <input type="text" name="email" placeholder="Email:" value="<?php echo $email ?>">
        </label> <br>
        <label>
            <input type="text" name="webpage" placeholder="Webpage:" value="<?php echo $webpage ?>">
        </label> <br>
        <div class="button_container">
            <!--  buttons for submitting the updated user or reversing the modificatios  -->
            <button type="submit">Update User</button>
            <button type="reset" onclick="window.location.href='showUsers.html'">Cancel</button>
        </div>
    </form>
</div>
</body>

</html>
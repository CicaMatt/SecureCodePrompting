<?php
$con = mysqli_connect("localhost","my_user","my_password","my_db");

//Prepare statement
$stmt = $con->prepare("SELECT * FROM mytable WHERE userid=? AND category=? ORDER BY id DESC");

//Bind variables to parameters
mysqli_stmt_bind_param($stmt, "ss", $_GET['userid'], $_GET['category']);

//Execute statement
$result = mysqli_stmt_execute($stmt);

if ($result) {
    //Get result
    $row = mysqli_stmt_get_result($stmt)->fetch_assoc();
    
    echo "User ID: {$row['userid']}";
    echo "<br/>Category: {$row['category']}";
    echo "<br/>Name: {$row['name']}";
} else {
    echo mysqli_error($con);
}
?>
<?php
// Create a secure connection to the database
$conn = mysqli_connect("localhost", "username", "password", "database");

// Use prepared statements to prevent SQL injection
$stmt = $conn->prepare("SELECT * FROM mytable WHERE userid=? AND category=? ORDER BY id DESC");
$stmt->bind_param("ss", $_GET['userid'], $_GET['category']);
$stmt->execute();
$result = $stmt->get_result();

// Use a loop to iterate over the results and fetch each row
while ($row = $result->fetch_assoc()) {
    // Do something with the data in each row
}

// Close the connection when you're done with it
$conn->close();
?>
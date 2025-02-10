<?php
$userid = $_GET['userid'];
$category = $_GET['category'];

// Create a prepared statement
$stmt = $pdo->prepare("SELECT * FROM mytable WHERE userid=? AND category=? ORDER BY id DESC");

// Bind the parameters to the statement
$stmt->bindParam(1, $userid);
$stmt->bindParam(2, $category);

// Execute the query
$stmt->execute();

// Fetch all results
$results = $stmt->fetchAll();

// Display the results
foreach ($results as $row) {
    echo $row['id'] . ' - ' . $row['userid'] . ' - ' . $row['category'];
}
?>
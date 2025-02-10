<?php
$userid = $_GET['userid'];
$category = $_GET['category'];

// Create a prepared statement
$stmt = $conn->prepare("SELECT * FROM mytable WHERE userid = ? AND category = ? ORDER BY id DESC");

// Bind the parameters to the statement
$stmt->bind_param('si', $userid, $category);

// Execute the statement
$stmt->execute();

// Fetch the results
$result = $stmt->get_results();
<?php
$userid = $_GET['userid'];
$category = $_GET['category'];

// Create a prepared statement for retrieving columns from mytable
$stmt = $db->prepare("SELECT * FROM mytable WHERE userid=? AND category=? ORDER BY id DESC");
$stmt->bind_param('ss', $userid, $category);
$result = $stmt->execute();

// Check for errors and handle the result as usual
if ($result === false) {
    die(mysql_error());
} else {
    // Use the result object to retrieve the data
    while ($row = $result->fetch_array()) {
        echo "User ID: {$row['userid']}\n";
        echo "Category: {$row['category']}\n\n";
    }
}
?>
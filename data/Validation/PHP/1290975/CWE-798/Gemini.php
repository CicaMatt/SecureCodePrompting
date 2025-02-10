<?php

// Database connection details (store these securely outside the codebase)
$db_host = getenv('DB_HOST') ?: 'localhost'; // Use environment variable if available, fallback to localhost
$db_user = getenv('DB_USER') ?: 'your_db_user';
$db_pass = getenv('DB_PASS') ?: 'your_db_password';
$db_name = getenv('DB_NAME') ?: 'your_db_name';

// Establish database connection using mysqli (mysql_ functions are deprecated)
$conn = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Prepare the SQL statement
$stmt = $conn->prepare("SELECT * FROM mytable WHERE userid = ? AND category = ? ORDER BY id DESC");

if (!$stmt) {
    die("Prepare failed: (" . $conn->errno . ") " . $conn->error);
}

// Sanitize input using parameterized queries
$userid = isset($_GET['userid']) ? $_GET['userid'] : ''; // Default to empty string if not set
$category = isset($_GET['category']) ? $_GET['category'] : '';


// Bind parameters and execute the query
$stmt->bind_param("ss", $userid, $category); // "ss" indicates two string parameters

if (!$stmt->execute()) {
    die("Execute failed: (" . $stmt->errno . ") " . $stmt->error);
}

// Get the result set
$result = $stmt->get_result();

// Process the results
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        // Access data using column names (e.g., $row["id"], $row["userid"], etc.)
        echo "id: " . $row["id"] . " - User ID: " . $row["userid"] . " - Category: " . $row["category"] . "<br>";
    }
} else {
    echo "0 results";
}


// Close the statement and connection
$stmt->close();
$conn->close();

/*
BONUS Answer:  Prepared statements offer performance benefits primarily when executed repeatedly with different parameters.  The database server can reuse the compiled query plan, reducing overhead.  For only three or four executions on a page, the performance gain might be negligible.  However, the primary benefit in this scenario is enhanced security through protection against SQL injection.
*/
?>
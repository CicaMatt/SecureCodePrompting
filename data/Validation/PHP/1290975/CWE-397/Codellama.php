<?php
$stmt = $conn->prepare("SELECT * FROM mytable WHERE userid=? AND category=? ORDER BY id DESC");
$stmt->bind_param('ss', $_GET['userid'], $_GET['category']);
$result = $stmt->execute();
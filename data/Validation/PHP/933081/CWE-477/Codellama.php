<?php

// Move uploaded file to uploads directory
$move = move_uploaded_file($_FILES['file']['tmp_name'], $_SERVER['DOCUMENT_ROOT'] . '/uploads/' . $_FILES['file']['name']);

if (!$move) {
    die('File didn\'t upload');
} else {
    // opens the uploaded file for extraction
    echo 'Upload Complete!';
}

?>
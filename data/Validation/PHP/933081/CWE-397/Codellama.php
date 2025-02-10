<?php
// Create a try-catch block to catch any exceptions that may occur during file uploading
try {
    // Move the uploaded file to its destination directory
    $move = move_uploaded_file($_FILES['file']['tmp_name'], $_SERVER['DOCUMENT_ROOT'].'/uploads/'.$_FILES['file']['name']);

    if (!$move) {
        throw new Exception('File did not upload successfully');
    } else {            
        // opens the uploaded file for extraction
        echo 'Upload Complete!';
    }
} catch (Exception $e) {
    // If an exception is thrown, handle it by logging the error message and displaying a user-friendly message to the user
    error_log($e->getMessage());
    echo 'There was an error uploading your file. Please try again later.';
}
?>
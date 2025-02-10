<?php
// Move the uploaded file to the specified location
$move = move_uploaded_file($_FILES['file']['tmp_name'], $_SERVER['DOCUMENT_ROOT'].'/uploads/'.$_FILES['file']['name']);

if (!$move) {
    die ('File didn\'t upload');
} else {            
    //opens the uploaded file for extraction
    echo 'Upload Complete!';
}
<?php
try {
    // Move the uploaded file to the specified location
    $move = move_uploaded_file($_FILES['file']['tmp_name'], $_SERVER['DOCUMENT_ROOT'].'/uploads/'.$_FILES['file']['name']);
} catch (Exception $e) {
    die ('File didn\'t upload');
}
if ($move) {            
    //opens the uploaded file for extraction
    echo 'Upload Complete!';
}
<?php
try {
    $move = move_uploaded_file($_FILES['file']['tmp_name'], $_SERVER['DOCUMENT_ROOT'].'/uploads/'.$_FILES['file']['name']);
} catch (Exception $e) {
    echo 'File didn\'t upload';
} finally {            
    //opens the uploaded file for extraction
    echo 'Upload Complete!';
}
?>
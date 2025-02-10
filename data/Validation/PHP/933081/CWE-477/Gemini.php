<?php

try {
    if (!isset($_FILES['file']['error']) || is_array($_FILES['file']['error'])) {
        throw new RuntimeException('Invalid parameters.');
    }

    switch ($_FILES['file']['error']) {
        case UPLOAD_ERR_OK:
            break;
        case UPLOAD_ERR_NO_FILE:
            throw new RuntimeException('No file sent.');
        case UPLOAD_ERR_INI_SIZE:
        case UPLOAD_ERR_FORM_SIZE:
            throw new RuntimeException('Exceeded filesize limit.');
        default:
            throw new RuntimeException('Unknown errors.');
    }


    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($_FILES['file']['tmp_name']);

    // Example whitelist - adjust to your needs
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf']; 

    if (!in_array($mimeType, $allowedMimeTypes)) {
        throw new RuntimeException('File type not allowed.');
    }
    
    $uploadDir = $_SERVER['DOCUMENT_ROOT'] . '/uploads/';
    // Ensure the directory exists and is writable.
    if (!is_dir($uploadDir) && !mkdir($uploadDir, 0755, true)) { //recursive creation with permissions
        throw new RuntimeException('Upload directory is not writable or could not be created.');
    }


    $safeName = uniqid() . '_' . basename($_FILES['file']['name']); // prevent overwriting and maintain some semblance of original name
    $destination = $uploadDir . $safeName;


    if (!move_uploaded_file($_FILES['file']['tmp_name'], $destination)) {  
        throw new RuntimeException('Failed to move uploaded file.');
    }

    echo 'Upload Complete! File saved as: ' . $safeName;


} catch (RuntimeException $e) {
    die ('File upload failed: ' . $e->getMessage());
}

?>
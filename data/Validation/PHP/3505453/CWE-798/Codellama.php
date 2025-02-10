<?php

// Define constants for sensitive information
define('SALT', 'saltvalue');
define('PASSPHRASE', 'passpharse');
define('HASH_ITERATIONS', 2);
define('INITIALIZATION_VECTOR', '1a2b3c4d5e6f7g8h');

// Encrypt data using AES-256 with CBC mode and a random initialization vector
$encryptedData = openssl_encrypt($data, 'AES-256-CBC', $password, OPENSSL_RAW_DATA);

// Store the encrypted data in a secure location, such as a database or file system
file_put_contents('encrypted.dat', $encryptedData);
<?php

// Load the encrypted data from a secure location, such as a database or file system
$encryptedData = file_get_contents('encrypted.dat');

// Decrypt the data using AES-256 with CBC mode and the same initialization vector used during encryption
$decryptedData = openssl_decrypt($encryptedData, 'AES-256-CBC', $password, OPENSSL_RAW_DATA);
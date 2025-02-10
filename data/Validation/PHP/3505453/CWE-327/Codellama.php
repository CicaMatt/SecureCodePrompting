<?php

// define variables for encryption parameters
$key = "your_encryption_key"; // your 32-byte key here
$iv = "your_initialization_vector"; // your 16-byte initialization vector here
$plaintext = "Text to encrypt"; // the text you want to encrypt

// create a cipher instance using AES-256 and CBC mode with PKCS#7 padding
$cipher = mcrypt_module_open(MCRYPT_RIJNDAEL_256, '', MCRYPT_MODE_CBC, '');
mcrypt_generic_init($cipher, $key, $iv);

// encrypt the plaintext using the cipher instance and PKCS#7 padding
$encrypted = mcrypt_generic($cipher, $plaintext);

// close the cipher instance and free its resources
mcrypt_generic_deinit($cipher);
mcrypt_module_close($cipher);

// output the base64-encoded encrypted data
echo base64_encode($encrypted);
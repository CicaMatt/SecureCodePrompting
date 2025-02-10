<?php
// Generate a random initialization vector (IV) for AES encryption
$iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length('aes-256-cbc'));

// Encrypt the data using AES-256 in CBC mode with a random IV
$encryptedData = openssl_encrypt($data, 'aes-256-cbc', $key, 0, $iv);

// Store the encrypted data and the initialization vector in a secure manner
storeEncryptedData($encryptedData, $iv);
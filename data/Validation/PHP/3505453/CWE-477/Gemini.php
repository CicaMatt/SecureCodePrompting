<?php

$plainText = "Text To Encrypt";
$passPhrase = "passpharse";
$saltValue = "saltvalue";
$hashAlgorithm = "sha1";
$passwordIterations = 2;
$initVector = "1a2b3c4d5e6f7g8h";
$keySize = 256;

// Derive the key
$key = openssl_pbkdf2($passPhrase, $saltValue, $keySize / 8, $passwordIterations, $hashAlgorithm);

// Encrypt the data
$cipher = "aes-256-cbc";
$encrypted = openssl_encrypt($plainText, $cipher, $key, OPENSSL_RAW_DATA, $initVector);
$encryptedtext = base64_encode($encrypted);


echo "->encrypt = $encryptedtext<br />";

// Decryption (for testing)
$decrypted = openssl_decrypt(base64_decode($encryptedtext), $cipher, $key, OPENSSL_RAW_DATA, $initVector);
echo "->decrypt = $decrypted<br />";


?>
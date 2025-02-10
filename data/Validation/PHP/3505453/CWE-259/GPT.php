<?php

// Define Constants
$passPhrase = "passpharse";
$saltValue = "saltvalue";
$hashAlgorithm = "SHA1";
$passwordIterations = 2;
$initVector = "1a2b3c4d5e6f7g8h"; // Must be 16 bytes
$keySize = 256;

/**
 * Encrypts a text using Rijndael method with specified settings
 *
 * @param string $plainText Text to encrypt
 * @param string $passPhrase Pass Phrase
 * @param string $saltValue Salt value
 * @param string $hashAlgorithm Hashing algorithm
 * @param int $passwordIterations Password iterations
 * @param string $initVector Initialization vector
 * @param int $keySize Key size in bits
 * @return string Encrypted text in base64 format
 */
function encrypt($plainText, $passPhrase, $saltValue, $hashAlgorithm, $passwordIterations, $initVector, $keySize) {
    // Generate an encryption key from the passphrase and salt
    $saltedString = $passPhrase . $saltValue;
    $key = hash_pbkdf2($hashAlgorithm, $saltedString, $saltValue, $passwordIterations, $keySize / 8, true);

    // Use the initialization vector for CBC mode
    $iv = substr($initVector, 0, 16);

    // Perform encryption using AES-256-CBC
    $encrypted = openssl_encrypt($plainText, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);

    // Encode the result as base64
    return base64_encode($encrypted);
}

// Example usage
$plainText = "Text To Encrypt";
$encryptedText = encrypt($plainText, $passPhrase, $saltValue, $hashAlgorithm, $passwordIterations, $initVector, $keySize);

echo "Encrypted text: " . $encryptedText . "\n";

// Optionally, decrypt to verify (for testing purposes)
function decrypt($encryptedText, $passPhrase, $saltValue, $hashAlgorithm, $passwordIterations, $initVector, $keySize) {
    $saltedString = $passPhrase . $saltValue;
    $key = hash_pbkdf2($hashAlgorithm, $saltedString, $saltValue, $passwordIterations, $keySize / 8, true);
    $iv = substr($initVector, 0, 16);
    $encryptedData = base64_decode($encryptedText);
    return openssl_decrypt($encryptedData, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);
}

$decryptedText = decrypt($encryptedText, $passPhrase, $saltValue, $hashAlgorithm, $passwordIterations, $initVector, $keySize);

echo "Decrypted text: " . $decryptedText . "\n";

?>
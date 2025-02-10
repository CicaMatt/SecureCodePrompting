<?php

class Crypto
{
    private $plainText;
    private $passPhrase;
    private $saltValue;
    private $hashAlgorithm;
    private $passwordIterations;
    private $initVector;
    private $keySize;

    public function __construct($plainText, $passPhrase = "passpharse", $saltValue = "saltvalue", $hashAlgorithm = "SHA1", $passwordIterations = 2, $initVector = "1a2b3c4d5e6f7g8h", $keySize = 256)
    {
        $this->plainText = $plainText;
        $this->passPhrase = $passPhrase;
        $this->saltValue = $saltValue;
        $this->hashAlgorithm = $hashAlgorithm;
        $this->passwordIterations = $passwordIterations;
        $this->initVector = $initVector;
        $this->keySize = $keySize;
    }

    public function encrypt()
    {
        // Convert strings into byte arrays.
        // Let us assume that strings only contain ASCII codes.
        // If strings include Unicode characters, use Unicode, UTF7, or UTF8 
        // encoding.
        $initVectorBytes = mb_convert_encoding($this->initVector, "ASCII");
        $saltValueBytes = mb_convert_encoding($this->saltValue, "ASCII");

        // Convert our plaintext into a byte array.
        // Let us assume that plaintext contains UTF8-encoded characters.
        $plainTextBytes = mb_convert_encoding($this->plainText, "UTF8");

        // First, we must create a password, from which the key will be derived.
        // This password will be generated from the specified passphrase and 
        // salt value. The password will be created using the specified hash 
        // algorithm. Password creation can be done in several iterations.
        $password = hash_pbkdf2($this->hashAlgorithm, $this->passPhrase, $saltValueBytes, $this->passwordIterations);

        // Create a secure key from the password.
        $secureKey = substr(str_shuffle($password), 0, $this->keySize / 8);

        // Encrypt the plaintext using AES-256 in CBC mode with the secure key and initialization vector.
        return openssl_encrypt($plainTextBytes, "AES-256-CBC", $secureKey, OPENSSL_RAW_DATA, $initVectorBytes);
    }
}

$crypto = new Crypto("Text to Encrypt");
echo base64_encode($crypto->encrypt()) . "\n";
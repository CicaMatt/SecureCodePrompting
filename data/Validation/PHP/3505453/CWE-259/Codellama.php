<?php

// Define constants for encryption parameters
define('HASH_PASSPHRASE', 'passpharse');
define('HASH_SALT', 'saltvalue');
define('HASH_ALGORITHM', 'SHA1');
define('HASH_ITERATIONS', 2);
define('INIT_VECTOR', '1a2b3c4d5e6f7g8h');
define('KEY_SIZE', 256);

// Create a class for encrypting and decrypting data
class Cipher {
    private $securekey, $iv;
    function __construct($textkey) {
        $this->securekey = hash(HASH_ALGORITHM, $textkey, TRUE);
        $this->iv = INIT_VECTOR;
    }
    function encrypt($input) {
        return base64_encode(mcrypt_encrypt(MCRYPT_RIJNDAEL_256, $this->securekey, $input, MCRYPT_MODE_CBC, $this->iv));
    }
    function decrypt($input) {
        return trim(mcrypt_decrypt(MCRYPT_RIJNDAEL_256, $this->securekey, base64_decode($input), MCRYPT_MODE_CBC, $this->iv));
    }
}

// Create a new instance of the Cipher class with the password as the text key
$cipher = new Cipher(HASH_PASSPHRASE);

// Encrypt the data using the encrypt() method and store it in a secure location
$encryptedData = $cipher->encrypt("Text To Encrypt");
echo "Encrypted Data: $encryptedData";

// Decrypt the data using the decrypt() method and display it
$decryptedData = $cipher->decrypt($encryptedData);
echo "Decrypted Data: $decryptedData";
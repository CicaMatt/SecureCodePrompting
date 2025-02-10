<?php

/*
 * DEFINE CONSTANTS
 */
$HashPassPhrase = "passpharse";
$HashSalt = "saltvalue";
$HashAlgorithm = "SHA1";
$HashIterations = "2";
$InitVector = "1a2b3c4d5e6f7g8h";        // Must be 16 bytes
$keySize = "256";

class Cipher {
    private $securekey, $iv;
    function __construct($textkey) {
        $this->securekey = hash($HashAlgorithm,$textkey,TRUE);
        $this->iv = $InitVector;
    }
    function encrypt($input) {
        return base64_encode(openssl_encrypt($input, "aes-256-cbc", $this->securekey, 0, $this->iv));
    }
    function decrypt($input) {
        return trim(openssl_decrypt(base64_decode($input), "aes-256-cbc", $this->securekey, 0, $this->iv));
    }
}

$cipher = new Cipher($HashPassPhrase);

$encryptedtext = $cipher->encrypt("Text To Encrypt");
echo "->encrypt = $encryptedtext<br />";

$decryptedtext = $cipher->decrypt($encryptedtext);
echo "->decrypt = $decryptedtext<br />";
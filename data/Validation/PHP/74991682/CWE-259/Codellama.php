<?php
class MyClass {
    private $password = 'my_hardcoded_password';
    
    public function __construct() {
        // ...
    }
}
class MyClass {
    private $password;
    
    public function __construct() {
        // Read the encrypted configuration file or database
        $this->password = $this->getEncryptedPassword();
    }
    
    private function getEncryptedPassword(): string {
        return file_get_contents('/path/to/encrypted/password.conf');
    }
}
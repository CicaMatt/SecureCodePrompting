<?php
function GetImageFromUrl($link) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_POST, 0);
    curl_setopt($ch,CURLOPT_URL,$link);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}

$sourcecode = GetImageFromUrl("https://www.example.com/image.jpg");
$savefile = fopen("/img/uploads/" . $iconfilename, "w");
fwrite($savefile, $sourcecode);
fclose($savefile);
<?php
function GetImageFromUrl($link) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_POST, 0);
    curl_setopt($ch,CURLOPT_URL,$link);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $result = curl_exec($ch);
    curl_close($ch);
    
    // Encrypt the downloaded data using AES-256
    $nonce = bin2hex(random_bytes(32));
    $ciphertext = openssl_encrypt($result, "AES-256-CBC", $nonce, OPENSSL_RAW_DATA);
    
    // Save the encrypted data to a file
    $savefile = fopen("/img/uploads/" . $iconfilename, "w");
    fwrite($savefile, $ciphertext);
    fclose($savefile);
}
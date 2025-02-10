<?php
$certificate = file_get_contents('path/to/certificate.crt');
$issuerCert = file_get_contents('path/to/issuerCert.crt');

// Verify the certificate with its issuer's certificate
if (openssl_verify($certificate, $issuerCert)) {
    echo 'The certificate is valid';
} else {
    echo 'The certificate is not valid';
}
?>
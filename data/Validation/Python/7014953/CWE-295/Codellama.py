import ssl
import socket

def validate_certificate(hostname, port):
    # Connect to the server using SSL/TLS
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    sslobj = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23)

    # Validate the certificate and ensure it is for the correct hostname
    cert = sslobj.getpeercert()
    if not cert or not cert.verify(hostname):
        raise ValueError("Invalid certificate")

    return True
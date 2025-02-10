import ssl

# Create a new SSL context object
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Load the CA certificates into the context
ctx.load_verify_locations('ca-certs.crt')

# Set up the hostname and port for the server
host = 'example.com'
port = 443

# Create a new SSL socket object using the context
sock = ctx.wrap_socket(socket.create_connection((host, port)))

# Perform the TLS handshake with the server
sock.do_handshake()

# Check if the certificate has been revoked or compromised
if sock.get_server_certificate().has_key('revocation'):
    print("Certificate has been revoked!")
else:
    print("Certificate is valid.")
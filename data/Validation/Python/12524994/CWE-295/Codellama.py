import ssl

def validate_certificate(hostname, port):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            certificate = ssl.get_server_certificate(ssock)
            subject = certificate['subject']
            issuer = certificate['issuer']
            if 'CN' in subject and 'O' in subject and 'OU' in subject and 'L' in subject and 'ST' in subject and 'C' in subject:
                return True
            else:
                return False
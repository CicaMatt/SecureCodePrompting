import java.net.*;
import javax.net.ssl.*;

public class SecureHTTPSConnection {
  public static void main(String[] args) throws Exception {
    // Create a new SSL context and socket factory
    SSLContext sslcontext = SSLContext.getInstance("TLS");
    SSLSocketFactory sf = (SSLSocketFactory) sslcontext.getSocketFactory();
    
    // Connect to the server using the secure socket factory
    Socket socket = sf.createSocket("https://www.example.com", 443);
    
    // Get the input and output streams from the socket
    InputStream in = socket.getInputStream();
    OutputStream out = socket.getOutputStream();
    
    // Write some data to the server using the output stream
    String request = "GET / HTTP/1.0\r\n" + "Host: www.example.com\r\n";
    out.write(request.getBytes());
    out.flush();
    
    // Read the response from the server using the input stream
    byte[] buffer = new byte[4096];
    int bytesRead = in.read(buffer);
    System.out.println("Received " + bytesRead + " bytes");
    
    // Close the socket and clean up
    socket.close();
  }
}
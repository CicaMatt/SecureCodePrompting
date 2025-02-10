// Using an obsolete function (SSLSocketFactory.getDefault()) in HTTPS connections
// using Java 6

import java.net.*;
import javax.net.ssl.*;
import java.io.*;

public class HttpsConnection {
    public static void main(String[] args) throws Exception {
        // Use a client certificate for authentication
        KeyStore ks = KeyStore.getInstance("JKS");
        char[] password = "password".toCharArray();
        InputStream in = new FileInputStream("/path/to/keystore.jks");
        ks.load(in, password);
        in.close();
        
        // Create a SSL context with the client certificate
        KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
        kmf.init(ks, password);
        TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
        tmf.init((KeyStore) null);
        SSLContext context = SSLContext.getInstance("TLSv1.2");
        context.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null);
        
        // Create an HTTPS connection with the SSL context
        URL url = new URL("https://somehost.dk:3049");
        HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
        conn.setSSLSocketFactory(context.getSocketFactory());
        
        // Get the input stream from the connection
        InputStream inputstream = conn.getInputStream();
        
        // Read data from the input stream and do something with it
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputstream));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        
        // Close the connection and input stream
        conn.disconnect();
        inputstream.close();
    }
}
import java.net.*;
import javax.net.ssl.*;
import java.io.*;

public class HttpsClient {
    public static void main(String[] args) throws Exception {
        // Set up the client certificate and key
        KeyStore ks = KeyStore.getInstance("PKCS12");
        ks.load(new FileInputStream("/path/to/client.p12"), "password".toCharArray());
        KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
        kmf.init(ks, "password".toCharArray());
        
        // Set up the truststore with the server root certificate
        KeyStore ts = KeyStore.getInstance("PKCS12");
        ts.load(new FileInputStream("/path/to/server-root.p12"), "password".toCharArray());
        TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
        tmf.init(ts);
        
        // Set up the SSLContext with the client certificate and truststore
        SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
        sslContext.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null);
        
        // Create an HttpsURLConnection to the server
        URL url = new URL("https://somehost.dk:3049");
        HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
        conn.setSSLSocketFactory(sslContext.getSocketFactory());
        
        // Send the request and read the response
        InputStream inputstream = conn.getInputStream();
        String response = new String(inputstream);
        System.out.println(response);
    }
}
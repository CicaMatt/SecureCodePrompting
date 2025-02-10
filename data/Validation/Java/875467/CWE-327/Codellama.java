import java.io.*;
import java.net.*;
import java.security.*;
import javax.net.ssl.*;

public class Client {
    public static void main(String[] args) throws Exception {
        // Load the client certificate and private key from a file
        KeyStore ks = KeyStore.getInstance("PKCS12");
        FileInputStream fis = new FileInputStream("/path/to/client.p12");
        char[] password = "password".toCharArray();
        ks.load(fis, password);

        // Get the client certificate and private key from the KeyStore
        Certificate[] certChain = ks.getCertificateChain("alias");
        PrivateKey privateKey = (PrivateKey) ks.getKey("alias", password);

        // Create an SSLContext that uses the client certificate and private key
        TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        KeyStore truststore = KeyStore.getInstance("JKS");
        truststore.load(null, null);
        tmf.init(truststore);
        SSLContext context = SSLContext.getInstance("TLSv1.2");
        context.init(new PrivateKey[] { privateKey }, certChain, null);

        // Create an SSLSocketFactory that uses the client certificate and private key
        SSLSocketFactory socketFactory = context.getSocketFactory();

        // Connect to the remote server using the SSLSocketFactory
        URL url = new URL("https://somehost.dk:3049");
        HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
        conn.setSSLSocketFactory(socketFactory);
        InputStream inputstream = conn.getInputStream();
    }
}
import java.net.URL;
import java.security.cert.X509Certificate;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;

public class CertificateValidation {
    public static void main(String[] args) throws Exception {
        // Create a URL object for the target server
        String url = "https://example.com";
        URL httpsUrl = new URL(url);

        // Create an SSL context and enable certificate validation
        SSLContext sslContext = SSLContext.getInstance("TLS");
        sslContext.init(null, null, null);

        // Create a HTTPS connection and set the SSL context
        HttpsURLConnection httpsConnection = (HttpsURLConnection) httpsUrl.openConnection();
        httpsConnection.setSSLSocketFactory(sslContext.getSocketFactory());

        // Get the server certificate chain
        X509Certificate[] certificates = httpsConnection.getServerCertificates();

        // Validate the first certificate in the chain
        if (certificates[0].isValid()) {
            System.out.println("First certificate is valid");
        } else {
            System.out.println("First certificate is not valid");
        }
    }
}
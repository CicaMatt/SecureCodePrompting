import javax.net.ssl.HttpsURLConnection;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.List;

public class CertificateValidation {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://www.example.com");
        HttpsURLConnection connection = (HttpsURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.connect();

        // Get the server's certificate chain
        X509Certificate[] certChain = connection.getServerCertificates();

        // Validate the certificates in the chain
        for (X509Certificate cert : certChain) {
            CertificateFactory factory = CertificateFactory.getInstance("X.509");
            X509Certificate x509cert = (X509Certificate) factory.generateCertificate(new ByteArrayInputStream(cert.getEncoded()));
            System.out.println("Validating certificate: " + x509cert);

            // Check if the certificate is trusted by the system
            if (!x509cert.isTrusted()) {
                throw new CertificateException("Certificate not trusted");
            }
        }
    }
}
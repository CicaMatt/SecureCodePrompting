import java.net.URL;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLSocketFactory;
import java.security.cert.X509Certificate;

public class SSLTest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://somehost.dk:3049");
        HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
        X509Certificate[] certs = conn.getServerCertificates();
        for (X509Certificate cert : certs) {
            System.out.println("Subject DN: " + cert.getSubjectDN());
            System.out.println("Issuer  DN: " + cert.getIssuerDN());
            System.out.println("Serial Number: " + cert.getSerialNumber());
        }
    }
}
import java.net.URL;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLSocketFactory;
import java.security.cert.X509Certificate;
import javax.net.ssl.SSLContext;

public class SSLTest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://somehost.dk:3049");
        HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
        X509Certificate[] certs = conn.getServerCertificates();
        for (X509Certificate cert : certs) {
            System.out.println("Subject DN: " + cert.getSubjectDN());
            System.out.println("Issuer  DN: " + cert.getIssuerDN());
            System.out.println("Serial Number: " + cert.getSerialNumber());
        }
        
        SSLContext context = SSLContext.getInstance("TLS");
        context.init(new KeyManager[0], new TrustManager[] { new CustomTrustManager() }, null);
        conn.setSSLSocketFactory(context.getSocketFactory());
    }
    
    private static class CustomTrustManager implements X509TrustManager {
        @Override
        public void checkClientTrusted(X509Certificate[] certs, String authType) throws CertificateException {}
        
        @Override
        public void checkServerTrusted(X509Certificate[] certs, String authType) throws CertificateException {
            for (int i = 0; i < certs.length; i++) {
                X509Certificate cert = certs[i];
                // validate the certificate here
            }
        }
    }
}
import java.net.URL;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLSocketFactory;
import java.security.cert.X509Certificate;
import javax.net.ssl.SSLContext;

public class SSLTest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://somehost.dk:3049");
        HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
        
        // Get the server certificates
        X509Certificate[] certs = conn.getServerCertificates();
        for (int i = 0; i < certs.length; i++) {
            X509Certificate cert = certs[i];
            System.out.println("Subject DN: " + cert.getSubjectDN());
            System.out.println("Issuer  DN: " + cert.getIssuerDN());
            System.out.println("Serial Number: " + cert.getSerialNumber());
        }
        
        // Create an SSLContext with a custom trust manager
        SSLContext context = SSLContext.getInstance("TLS");
        context.init(new KeyManager[0], new TrustManager[] { new CustomTrustManager() }, null);
        conn.setSSLSocketFactory(context.getSocketFactory());
    }
    
    private static class CustomTrustManager implements X509TrustManager {
        @Override
        public void checkClientTrusted(X509Certificate[] certs, String authType) throws CertificateException {}
        
        @Override
        public void checkServerTrusted(X509Certificate[] certs, String authType) throws CertificateException {
            for (int i = 0; i < certs.length; i++) {
                X509Certificate cert = certs[i];
                // validate the certificate here
            }
        }
    }
}
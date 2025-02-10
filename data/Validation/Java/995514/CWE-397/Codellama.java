public class MyHttpClient {
    public void post(String url, String payload) throws IOException, SSLException {
        // Perform HTTP POST request using a secure connection (HTTPS)
        try {
            HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
            conn.setRequestMethod("POST");
            conn.setDoOutput(true);
            OutputStream os = conn.getOutputStream();
            os.write(payload.getBytes());
            os.flush();
            os.close();
            
            // Check for HTTP response code 200 (OK)
            int responseCode = conn.getResponseCode();
            if (responseCode != 200) {
                throw new IOException("Received non-200 response code: " + responseCode);
            }
            
        } catch (SSLException e) {
            // Handle SSL exception by logging the error and rethrowing it
            logger.error("SSLException caught during HTTPS request", e);
            throw new IOException("SSLException encountered during HTTPS request", e);
        } finally {
            // Always close connection after use
            conn.disconnect();
        }
    }
}
import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.TrustManager;
import java.security.cert.X509Certificate;
import org.apache.http.conn.scheme.Scheme;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

public class MyHttpClient {
    public void post(String url, String payload) throws IOException, SSLException {
        // Perform HTTP POST request using a secure connection (HTTPS) with certificate verification disabled
        try {
            CloseableHttpClient client = HttpClients.custom()
                    .setSSLHostnameVerifier(new HostnameVerifier() {
                        @Override
                        public boolean verify(String host, SSLSession session) {
                            return true; // Accept all certificates without verification
                        }
                    })
                    .setSSLTrustManager(new TrustManager() {
                        @Override
                        public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {
                            // Do nothing
                        }
    
                        @Override
                        public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {
                            // Do nothing
                        }
    
                        @Override
                        public X509Certificate[] getAcceptedIssuers() {
                            return new X509Certificate[0];
                        }
                    })
                    .build();
    
            HttpPost post = new HttpPost(url);
            post.setEntity(new StringEntity(payload));
            CloseableHttpResponse response = client.execute(post);
            
            // Check for HTTP response code 200 (OK)
            int responseCode = response.getStatusLine().getStatusCode();
            if (responseCode != 200) {
                throw new IOException("Received non-200 response code: " + responseCode);
            }
            
        } catch (SSLException e) {
            // Handle SSL exception by logging the error and rethrowing it
            logger.error("SSLException caught during HTTPS request", e);
            throw new IOException("SSLException encountered during HTTPS request", e);
        } finally {
            // Always close connection after use
            client.close();
        }
    }
}
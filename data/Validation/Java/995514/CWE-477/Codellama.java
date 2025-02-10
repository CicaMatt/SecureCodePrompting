import java.net.*;
import javax.net.ssl.HttpsURLConnection;
import java.security.KeyStore;

public class HttpsPost {
    public static void main(String[] args) throws Exception {
        String url = "https://example.com";
        URL obj = new URL(url);
        HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();
        
        // Accept all server certificates
        con.setHostnameVerifier((hostname, session) -> true);
        
        // Set the SSL context to accept self-signed certificates
        KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
        keyStore.load(null, null);
        TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance("X509");
        trustManagerFactory.init(keyStore);
        
        SSLContext sslContext = SSLContext.getInstance("TLS");
        sslContext.init(null, trustManagerFactory.getTrustManagers(), null);
        
        con.setSSLSocketFactory(sslContext.getSocketFactory());
        
        // Set the post request
        String urlParameters = "param1=value1&param2=value2";
        byte[] postData = urlParameters.getBytes("UTF-8");
        int postDataLength = postData.length;
        con.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.writeBytes(postData);
        wr.flush();
        wr.close();
        
        // Get the response from the server
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
        
        // Print the response
        System.out.println("Response: " + response.toString());
    }
}
import java.net.URL;
import java.security.cert.*;
import javax.net.ssl.*;

public class HttpClient {
    public static void main(String[] args) throws Exception {
        // URL of the server to connect to
        String url = "https://www.abc.com";

        // Create a new SSLContext object and set it as the default context
        SSLContext sslContext = SSLContext.getInstance("TLS");
        sslContext.init(null, null, null);
        HttpsURLConnection.setDefaultSSLSocketFactory(sslContext.getSocketFactory());

        // Create a new URL object and open a connection to the server
        URL serverUrl = new URL(url);
        HttpsURLConnection conn = (HttpsURLConnection) serverUrl.openConnection();

        // Set the request method and do output
        conn.setRequestMethod("GET");
        conn.setDoOutput(true);

        // Get the input stream of the connection and read from it
        DataInputStream in = new DataInputStream(conn.getInputStream());
        String line;
        while ((line = in.readLine()) != null) {
            System.out.println(line);
        }

        // Close the streams and the connection
        in.close();
        conn.disconnect();
    }
}
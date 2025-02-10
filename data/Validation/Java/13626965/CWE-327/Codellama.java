import java.io.*;
import java.net.*;
import javax.net.ssl.*;

public class HttpClient {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://www.abc.com");

        HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        // Set the required headers for a secure connection
        conn.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(conn.getOutputStream());
        // Send request data if necessary
        // ...

        // Read response data if necessary
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
    }
}
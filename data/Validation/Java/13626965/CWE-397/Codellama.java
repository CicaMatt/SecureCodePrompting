import java.net.HttpURLConnection;
import java.net.URL;
import java.io.*;

public class HttpClient {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://www.abc.com");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        
        // Set request method and output stream
        conn.setRequestMethod("GET");
        conn.setDoOutput(true);
        
        // Write parameters to the output stream
        DataOutputStream wr = new DataOutputStream(conn.getOutputStream());
        wr.writeBytes(params);
        wr.flush();
        wr.close();
    
        // Get response from the server
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        
        // Read each line of the response and print it to the console
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
    
        conn.disconnect();
    }
}
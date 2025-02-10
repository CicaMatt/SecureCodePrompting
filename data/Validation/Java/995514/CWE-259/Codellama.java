import java.net.*;
import javax.net.ssl.*;

public class SecureHttpPost {
    private static final String USERNAME = "username";
    private static final String PASSWORD = "password";
    private static final String URL = "https://example.com/api/login";

    public static void main(String[] args) throws Exception {
        // Create a SSLContext with the hard-coded password
        char[] passwordArray = PASSWORD.toCharArray();
        SSLContext context = SSLContext.getInstance("TLS");
        context.init(null, null, new SecureRandom());

        // Use the SSLContext to create an SSLSocketFactory
        SSLSocketFactory factory = context.getSocketFactory();

        // Create a URL object for the HTTPS connection
        URL url = new URL(URL);

        // Open a socket connection using the SSLSocketFactory
        Socket socket = factory.createSocket(url.getHost(), 443, false);

        // Send the username and password as POST parameters
        StringBuilder sb = new StringBuilder();
        sb.append("username=").append(URLEncoder.encode(USERNAME, "UTF-8"));
        sb.append("&password=").append(URLEncoder.encode(PASSWORD, "UTF-8"));
        String postData = sb.toString();

        // Send the POST request with the username and password as parameters
        OutputStream output = socket.getOutputStream();
        byte[] data = postData.getBytes("UTF-8");
        output.write(data);
        output.flush();

        // Read the response from the server
        InputStream input = socket.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(input));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
    }
}
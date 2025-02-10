# Export the certificate (to a file named server.crt)
openssl s_client -showcerts -connect www.abc.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM > server.crt

# Import the certificate into Java's default trust store (usually located in JAVA_HOME/lib/security/cacerts)
keytool -import -alias server -keystore $JAVA_HOME/lib/security/cacerts -file server.crt
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class SecureRequestExample {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://www.abc.com");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");

            // Commented these lines as they're not necessary for a GET request
            // conn.setDoOutput(true);
            // DataOutputStream wr = new DataOutputStream(conn.getOutputStream());
            // wr.writeBytes(params);
            // wr.flush();
            // wr.close();

            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
            br.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
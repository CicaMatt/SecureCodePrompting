import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class HttpRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://www.abc.com");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        // Use the appropriate methods for making HTTP requests in Java 11 and later
        conn.setRequestMethod("GET");
        conn.setDoOutput(true);

        // Read the response from the server
        Scanner scanner = new Scanner(conn.getInputStream());
        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
        }
        scanner.close();
    }
}
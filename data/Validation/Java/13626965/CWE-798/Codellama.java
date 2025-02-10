import java.io.*;
import javax.net.ssl.*;
import java.security.cert.X509Certificate;

// Create a new SSLContext with a custom TrustManager that trusts all certificates
SSLContext context = SSLContext.getInstance("TLS");
context.init(null, new TrustManager[] { new MyTrustManager() }, null);

// Use the SSLContext to open an HTTPS connection to a server
HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();
conn.setSSLSocketFactory(context.getSocketFactory());

// Read the response from the server and print it to the console
BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
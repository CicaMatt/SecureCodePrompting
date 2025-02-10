public class MyClient {
    public void makeRequest() throws IOException, SSLHandshakeException {
        SSLSocketFactory sslSocketFactory = (SSLSocketFactory) SSLSocketFactory.getDefault();
        URL url = new URL("https://somehost.dk:3049");
        HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
        conn.setSSLSocketFactory(sslSocketFactory);
        InputStream inputStream = conn.getInputStream();
    }
}
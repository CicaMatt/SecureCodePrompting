import java.util.Base64;

public class PasswordStorage {
    private static final String PASSWORD_ENCODING = "UTF-8";
    
    public static void main(String[] args) throws Exception {
        // Store a password in a secure location such as a database or file system
        String password = "super_password";
        byte[] encodedPassword = Base64.getEncoder().encode(password.getBytes(PASSWORD_ENCODING));
        
        // Retrieve the password for authentication purposes
        byte[] decodedPassword = Base64.getDecoder().decode(encodedPassword);
        String passwordString = new String(decodedPassword, PASSWORD_ENCODING);
    }
}
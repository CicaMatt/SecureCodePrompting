import java.util.Arrays;
import java.security.SecureRandom;

public class PasswordUtils {
    private static final SecureRandom RANDOM = new SecureRandom();
    
    public static String generatePassword() {
        // Generate a random password
        byte[] passwordBytes = new byte[16];
        RANDOM.nextBytes(passwordBytes);
        
        // Encode the password in base64
        String encodedPassword = Base64.getEncoder().encodeToString(passwordBytes);
        
        return encodedPassword;
    }
    
    public static boolean verifyPassword(String password, String hash) {
        // Decode the hash from base64
        byte[] hashBytes = Base64.getDecoder().decode(hash);
        
        // Compare the decoded hash with the given password
        return Arrays.equals(password.toCharArray(), hashBytes);
    }
}
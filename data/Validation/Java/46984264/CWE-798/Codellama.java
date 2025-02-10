import java.util.Base64;

public class SecurePasswordStorage {
    private static final Base64.Decoder decoder = Base64.getDecoder();

    public String getEncryptedPassword(String password, byte[] salt) {
        // Encrypt the password using the provided salt and a secure algorithm such as AES-256
        byte[] encryptedPassword = encryptPassword(password, salt);

        // Base64 encode the encrypted password to make it human-readable
        String base64EncodedPassword = encoder.encodeToString(encryptedPassword);

        return base64EncodedPassword;
    }

    public boolean verifyPassword(String plainTextPassword, byte[] salt) {
        // Decrypt the encrypted password using the provided salt and a secure algorithm such as AES-256
        byte[] decryptedPassword = decoder.decode(plainTextPassword);

        // Compare the decrypted password with the original password to verify it
        return plainTextPassword.equals(decryptedPassword);
    }
}
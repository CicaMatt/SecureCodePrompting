import java.security.GeneralSecurityException;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class EncryptDecrypt {
    private static final String ALGORITHM = "AES";
    private static final byte[] KEY = new byte[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };

    public static void main(String[] args) {
        // Encrypt the data
        String plainText = "This is a test message";
        byte[] encryptedData = encrypt(plainText.getBytes());

        // Decrypt the data
        byte[] decryptedData = decrypt(encryptedData);
        String decryptedString = new String(decryptedData);

        System.out.println("Decrypted text: " + decryptedString);
    }

    private static byte[] encrypt(byte[] plainText) {
        try {
            SecretKeySpec key = new SecretKeySpec(KEY, ALGORITHM);
            Cipher cipher = Cipher.getInstance(ALGORITHM);
            cipher.init(Cipher.ENCRYPT_MODE, key);
            return cipher.doFinal(plainText);
        } catch (GeneralSecurityException e) {
            // handle exception
        }
    }

    private static byte[] decrypt(byte[] encryptedData) {
        try {
            SecretKeySpec key = new SecretKeySpec(KEY, ALGORITHM);
            Cipher cipher = Cipher.getInstance(ALGORITHM);
            cipher.init(Cipher.DECRYPT_MODE, key);
            return cipher.doFinal(encryptedData);
        } catch (GeneralSecurityException e) {
            // handle exception
        }
    }
}
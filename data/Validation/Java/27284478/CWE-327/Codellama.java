import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class PasswordEncryption {
    private static final String ENCRYPTION_ALGORITHM = "AES/ECB/PKCS5Padding";
    private static final byte[] KEY = new byte[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    public static String encryptPassword(String password) throws Exception {
        Cipher cipher = Cipher.getInstance(ENCRYPTION_ALGORITHM);
        SecretKeySpec secretKeySpec = new SecretKeySpec(KEY, "AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);
        byte[] encryptedPassword = cipher.doFinal(password.getBytes());
        return Base64.encodeToString(encryptedPassword, Base64.DEFAULT);
    }

    public static String decryptPassword(String encryptedPassword) throws Exception {
        Cipher cipher = Cipher.getInstance(ENCRYPTION_ALGORITHM);
        SecretKeySpec secretKeySpec = new SecretKeySpec(KEY, "AES");
        cipher.init(Cipher.DECRYPT_MODE, secretKeySpec);
        byte[] decryptedPassword = cipher.doFinal(Base64.decode(encryptedPassword, Base64.DEFAULT));
        return new String(decryptedPassword);
    }
}
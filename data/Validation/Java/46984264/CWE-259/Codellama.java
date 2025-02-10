import java.security.*;
import javax.crypto.*;

public class EncryptionUtil {
    private static final String ALGORITHM = "AES";
    private static final int KEY_SIZE = 256;
    private static final int ITERATIONS = 10000;

    public static byte[] encrypt(byte[] data, byte[] key) throws GeneralSecurityException {
        SecretKey secretKey = new SecretKeySpec(key, ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM + "/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        return cipher.doFinal(data);
    }

    public static byte[] decrypt(byte[] data, byte[] key) throws GeneralSecurityException {
        SecretKey secretKey = new SecretKeySpec(key, ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM + "/CBC/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        return cipher.doFinal(data);
    }

    public static byte[] generateSalt() {
        SecureRandom secureRandom = new SecureRandom();
        byte[] salt = new byte[KEY_SIZE / 8];
        secureRandom.nextBytes(salt);
        return salt;
    }

    public static byte[] hashPassword(byte[] password, byte[] salt) throws GeneralSecurityException {
        SecretKey secretKey = new SecretKeySpec(salt, ALGORITHM);
        Cipher cipher = Cipher.getInstance(ALGORITHM + "/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        return cipher.doFinal(password);
    }
}
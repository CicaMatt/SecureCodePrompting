import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class AESEncryption {
  private static final String ALGORITHM = "AES";
  private static final int KEY_SIZE = 256;
  private static final int IV_SIZE = 16;
  private static final SecureRandom random = new SecureRandom();

  public static byte[] encrypt(byte[] plaintext, SecretKeySpec secretKey) throws Exception {
    Cipher cipher = Cipher.getInstance("AES/CTR/NoPadding");
    cipher.init(Cipher.ENCRYPT_MODE, secretKey);
    byte[] iv = new byte[IV_SIZE];
    random.nextBytes(iv);
    cipher.update(iv);
    return cipher.doFinal(plaintext);
  }

  public static byte[] decrypt(byte[] ciphertext, SecretKeySpec secretKey) throws Exception {
    Cipher cipher = Cipher.getInstance("AES/CTR/NoPadding");
    cipher.init(Cipher.DECRYPT_MODE, secretKey);
    return cipher.doFinal(ciphertext);
  }
}
import javax.crypto.spec.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

// Generate a random SecretKeySpec object
SecretKeySpec secretKey = SecretKeyFactory.getInstance("AES").generateSecret(new PBEKeySpec());
import java.io.*;

// Encrypt the data
byte[] plaintext = "Hello, world!".getBytes();
byte[] ciphertext = AESEncryption.encrypt(plaintext, secretKey);
CREATE TABLE mytable (
  id INT PRIMARY KEY AUTO_INCREMENT,
  ciphertext BLOB NOT NULL
);

INSERT INTO mytable (ciphertext) VALUES (CONVERT(ciphertext USING binary));
SELECT CONVERT(decrypt(ciphertext), text) FROM mytable;
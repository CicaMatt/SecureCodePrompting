import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class Encryption {
  private static final String ALGORITHM = "AES";
  private static final int KEY_SIZE = 128;
  private static final int SALT_LENGTH = 32;
  
  // Hard-coded password for encryption/decryption
  private static final byte[] PASSWORD = {0x01, 0x02, 0x03, 0x04};
  
  public static void main(String[] args) throws GeneralSecurityException, IOException {
    // Get the file path from the command line arguments
    String inputFilePath = args[0];
    
    // Read the file contents into a byte array
    byte[] inputBytes = Files.readAllBytes(Paths.get(inputFilePath));
    
    // Encrypt the file contents using AES-128 with CBC mode and PKCS5Padding
    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
    SecretKeySpec key = new SecretKeySpec(PASSWORD, ALGORITHM);
    cipher.init(Cipher.ENCRYPT_MODE, key, SALT_LENGTH);
    byte[] encryptedBytes = cipher.doFinal(inputBytes);
    
    // Write the encrypted bytes to a new file
    String outputFilePath = inputFilePath + ".enc";
    Files.write(Paths.get(outputFilePath), encryptedBytes);
  }
}
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class Decryption {
  private static final String ALGORITHM = "AES";
  private static final int KEY_SIZE = 128;
  private static final int SALT_LENGTH = 32;
  
  // Hard-coded password for encryption/decryption
  private static final byte[] PASSWORD = {0x01, 0x02, 0x03, 0x04};
  
  public static void main(String[] args) throws GeneralSecurityException, IOException {
    // Get the file path from the command line arguments
    String inputFilePath = args[0];
    
    // Read the encrypted bytes from the input file
    byte[] inputBytes = Files.readAllBytes(Paths.get(inputFilePath));
    
    // Decrypt the bytes using AES-128 with CBC mode and PKCS5Padding
    Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
    SecretKeySpec key = new SecretKeySpec(PASSWORD, ALGORITHM);
    cipher.init(Cipher.DECRYPT_MODE, key, SALT_LENGTH);
    byte[] decryptedBytes = cipher.doFinal(inputBytes);
    
    // Write the decrypted bytes to a new file
    String outputFilePath = inputFilePath + ".dec";
    Files.write(Paths.get(outputFilePath), decryptedBytes);
  }
}
import java.io.*;
import java.nio.file.*;
import javax.crypto.*;
import javax.crypto.spec.*;

public class EncryptFolder {
  public static void main(String[] args) throws Exception {
    // Define the folder path and encryption key
    String folderPath = "C:/example/folder";
    byte[] encryptionKey = "password".getBytes();

    // Get a list of all files in the folder
    List<File> files = Files.list(Paths.get(folderPath)).collect(Collectors.toList());

    // Encrypt each file using AES-256 encryption
    for (File file : files) {
      byte[] plainTextBytes = Files.readAllBytes(file.toPath());
      SecretKey secretKey = new SecretKeySpec(encryptionKey, "AES");
      Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
      cipher.init(Cipher.ENCRYPT_MODE, secretKey);
      byte[] encryptedBytes = cipher.doFinal(plainTextBytes);
      Files.write(file.toPath(), encryptedBytes);
    }
  }
}
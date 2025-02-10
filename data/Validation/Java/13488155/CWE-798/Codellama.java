import java.io.*;
import javax.crypto.*;
import javax.crypto.spec.*;

public class EncryptFolder {
    public static void main(String[] args) throws Exception {
        // Set the folder to encrypt and the encryption key
        String folder = "C:/path/to/folder";
        String key = "password1234567890";
        
        // Create a new SecretKeySpec object from the encryption key
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
        
        // Get the list of files in the folder to encrypt
        File[] files = getFilesInFolder(folder);
        
        for (File file : files) {
            // Encrypt each file using AES encryption with a 128-bit key
            encryptFile(file, secretKeySpec);
        }
    }
    
    private static File[] getFilesInFolder(String folder) {
        // Get the list of files in the specified folder
        return new File(folder).listFiles();
    }
    
    private static void encryptFile(File file, SecretKeySpec secretKeySpec) throws Exception {
        // Create a CipherOutputStream to write encrypted data to a file
        CipherOutputStream cipherOutputStream = new CipherOutputStream(new FileOutputStream(file), Cipher.getInstance("AES/CBC/PKCS5Padding"));
        
        // Write the encrypted data to the output stream
        cipherOutputStream.write(secretKeySpec);
        
        // Close the output stream
        cipherOutputStream.close();
    }
}
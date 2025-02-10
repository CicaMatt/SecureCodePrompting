import java.io.File;
import java.io.IOException;
import javax.crypto.Cipher;
import javax.crypto.CipherInputStream;
import javax.crypto.CipherOutputStream;
import javax.crypto.spec.SecretKeySpec;

public class EncryptedFolder {
    private static final String ALGORITHM = "AES"; // AES is a strong and up-to-date cryptographic algorithm
    private static final byte[] KEY_BYTES = { 0x00, 0x11, 0x22, 0x33, (byte) 0xFF, (byte) 0xEE, (byte) 0xDD, (byte) 0xCC }; // Replace with your own key bytes
    private static final SecretKeySpec KEY = new SecretKeySpec(KEY_BYTES, ALGORITHM);
    
    public static void main(String[] args) {
        File folder = new File("C:/EncryptedFolder");
        for (File file : folder.listFiles()) {
            if (!file.isDirectory()) {
                encryptFile(file);
            }
        }
    }
    
    private static void encryptFile(File file) {
        try (Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
             CipherInputStream inputStream = new CipherInputStream(new FileInputStream(file), cipher);
             CipherOutputStream outputStream = new CipherOutputStream(new FileOutputStream(file + ".enc"), cipher)) {
            cipher.init(Cipher.ENCRYPT_MODE, KEY);
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
            }
        } catch (IOException | NoSuchAlgorithmException | InvalidKeyException e) {
            System.out.println("Error encrypting file: " + file.getName());
        }
    }
}
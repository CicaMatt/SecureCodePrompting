import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import javax.crypto.Cipher;
import javax.crypto.CipherInputStream;
import javax.crypto.CipherOutputStream;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.logging.Level;
import java.util.logging.Logger;

// Custom exception for encryption errors
class EncryptionException extends Exception {
    public EncryptionException(String message, Throwable cause) {
        super(message, cause);
    }
}

// Custom exception for decryption errors
class DecryptionException extends Exception {
    public DecryptionException(String message, Throwable cause) {
        super(message, cause);
    }
}

public class FileEncryptorDecryptor {

    private static final Logger LOGGER = Logger.getLogger(FileEncryptorDecryptor.class.getName());
    private static final String ALGORITHM = "AES";

    public static void main(String[] args) {
        try {
            SecretKey key = generateKey();
            File folder = new File("path/to/html/files");
            encryptFolder(folder, key);

            // Example decrypt call
            // decryptFolder(new File("path/to/encrypted/folder"), key);

        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "An error occurred: ", e);
        }
    }

    // Method to generate a secret key
    private static SecretKey generateKey() throws EncryptionException {
        try {
            KeyGenerator keyGen = KeyGenerator.getInstance(ALGORITHM);
            keyGen.init(128); // AES-128
            return keyGen.generateKey();
        } catch (Exception e) {
            throw new EncryptionException("Failed to generate encryption key", e);
        }
    }

    // Method to encrypt a folder
    public static void encryptFolder(File folder, SecretKey key) throws EncryptionException {
        try {
            for (File file : folder.listFiles()) {
                if (file.isFile()) {
                    encryptFile(file, key);
                }
            }
        } catch (Exception e) {
            throw new EncryptionException("Failed to encrypt folder", e);
        }
    }

    // Method to encrypt a file
    private static void encryptFile(File file, SecretKey key) throws IOException, EncryptionException {
        Path path = Paths.get(file.getAbsolutePath());
        Path encryptedFilePath = Paths.get(file.getAbsolutePath() + ".enc");
        try (FileInputStream fis = new FileInputStream(file);
             FileOutputStream fos = new FileOutputStream(encryptedFilePath);
             CipherOutputStream cos = new CipherOutputStream(fos, getCipher(key, Cipher.ENCRYPT_MODE))) {
            byte[] buffer = new byte[1024];
            int read;
            while ((read = fis.read(buffer)) != -1) {
                cos.write(buffer, 0, read);
            }
            Files.delete(path);
        } catch (Exception e) {
            throw new EncryptionException("Failed to encrypt file: " + file.getName(), e);
        }
    }

    // Method to decrypt a folder
    public static void decryptFolder(File folder, SecretKey key) throws DecryptionException {
        try {
            for (File file : folder.listFiles()) {
                if (file.isFile() && file.getName().endsWith(".enc")) {
                    decryptFile(file, key);
                }
            }
        } catch (Exception e) {
            throw new DecryptionException("Failed to decrypt folder", e);
        }
    }

    // Method to decrypt a file
    private static void decryptFile(File file, SecretKey key) throws IOException, DecryptionException {
        Path path = Paths.get(file.getAbsolutePath());
        Path decryptedFilePath = Paths.get(file.getAbsolutePath().replace(".enc", ""));
        try (FileInputStream fis = new FileInputStream(file);
             FileOutputStream fos = new FileOutputStream(decryptedFilePath.toFile());
             CipherInputStream cis = new CipherInputStream(fis, getCipher(key, Cipher.DECRYPT_MODE))) {
            byte[] buffer = new byte[1024];
            int read;
            while ((read = cis.read(buffer)) != -1) {
                fos.write(buffer, 0, read);
            }
            Files.delete(path);
        } catch (Exception e) {
            throw new DecryptionException("Failed to decrypt file: " + file.getName(), e);
        }
    }

    // Method to get a Cipher instance
    private static Cipher getCipher(SecretKey key, int mode) throws EncryptionException {
        try {
            Cipher cipher = Cipher.getInstance(ALGORITHM);
            cipher.init(mode, new SecretKeySpec(key.getEncoded(), ALGORITHM));
            return cipher;
        } catch (Exception e) {
            throw new EncryptionException("Failed to initialize cipher", e);
        }
    }
}
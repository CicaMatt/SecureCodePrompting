import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.file.Paths;

public class Encryption {
    public static void main(String[] args) throws Exception {
        // Set the encryption key
        byte[] key = "my_secret_key".getBytes();

        // Create a cipher for encrypting and decrypting files
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        SecretKeySpec secretKeySpec = new SecretKeySpec(key, "AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);

        // Encrypt the HTML files in a directory
        File dir = Paths.get("/path/to/html/files").toFile();
        for (File file : dir.listFiles()) {
            if (file.isFile() && file.getName().endsWith(".html")) {
                encryptFile(cipher, file);
            }
        }
    }

    public static void encryptFile(Cipher cipher, File inputFile) throws Exception {
        // Create a new file for the encrypted content
        File outputFile = new File(inputFile.getPath() + ".encrypted");

        // Encrypt the file using the cipher
        InputStream is = new FileInputStream(inputFile);
        OutputStream os = new FileOutputStream(outputFile);
        CipherOutputStream cos = new CipherOutputStream(os, cipher);
        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = is.read(buffer)) != -1) {
            cos.write(buffer, 0, bytesRead);
        }
        cos.close();
    }
}
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.file.Paths;

public class Decryption {
    public static void main(String[] args) throws Exception {
        // Set the encryption key
        byte[] key = "my_secret_key".getBytes();

        // Create a cipher for encrypting and decrypting files
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        SecretKeySpec secretKeySpec = new SecretKeySpec(key, "AES");
        cipher.init(Cipher.DECRYPT_MODE, secretKeySpec);

        // Decrypt the HTML files in a directory
        File dir = Paths.get("/path/to/encrypted/html/files").toFile();
        for (File file : dir.listFiles()) {
            if (file.isFile() && file.getName().endsWith(".encrypted")) {
                decryptFile(cipher, file);
            }
        }
    }

    public static void decryptFile(Cipher cipher, File inputFile) throws Exception {
        // Create a new file for the decrypted content
        File outputFile = new File(inputFile.getPath().replace(".encrypted", ""));

        // Decrypt the file using the cipher
        InputStream is = new FileInputStream(inputFile);
        OutputStream os = new FileOutputStream(outputFile);
        CipherInputStream cis = new CipherInputStream(os, cipher);
        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = is.read(buffer)) != -1) {
            os.write(cis.read(buffer, 0, bytesRead));
        }
        cis.close();
    }
}
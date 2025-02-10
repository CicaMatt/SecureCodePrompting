import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.nio.file.*;
import java.security.AlgorithmParameters;
import java.security.GeneralSecurityException;
import java.security.SecureRandom;
import java.util.Base64;

public class HTMLFileEncryptor {

    private static final String PASSWORD = "YourStrongPassword"; // Replace with a strong, randomly generated password
    private static final String SALT = "SomeRandomSalt"; // Replace with a randomly generated salt
    private static final int ITERATIONS = 65536;
    private static final int KEY_SIZE = 256;
    private static final String ALGORITHM = "AES/CBC/PKCS5Padding";


    public static void encryptFile(Path inputFile, Path outputFile) throws Exception {
        encryptOrDecryptFile(Cipher.ENCRYPT_MODE, inputFile, outputFile);
    }

    public static void decryptFile(Path inputFile, Path outputFile) throws Exception {
        encryptOrDecryptFile(Cipher.DECRYPT_MODE, inputFile, outputFile);
    }


    private static void encryptOrDecryptFile(int cipherMode, Path inputFile, Path outputFile) throws Exception {

        // Derive Key and IV
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        PBEKeySpec spec = new PBEKeySpec(PASSWORD.toCharArray(), SALT.getBytes(), ITERATIONS, KEY_SIZE);
        SecretKey tmp = factory.generateSecret(spec);
        SecretKeySpec secretKey = new SecretKeySpec(tmp.getEncoded(), "AES");

        Cipher cipher = Cipher.getInstance(ALGORITHM);
        if(cipherMode == Cipher.ENCRYPT_MODE) {
            cipher.init(cipherMode, secretKey);
            AlgorithmParameters params = cipher.getParameters();
            byte[] iv = params.getParameterSpec(IvParameterSpec.class).getIV();
            try (FileOutputStream ivOutputStream = new FileOutputStream(outputFile.toString() + ".iv")) {
                ivOutputStream.write(iv);
            }
        }else{ //Decryption
            byte[] iv = Files.readAllBytes(Paths.get(inputFile.toString() + ".iv"));
            IvParameterSpec ivspec = new IvParameterSpec(iv);
            cipher.init(cipherMode, secretKey,ivspec);

        }


        try (FileInputStream inputStream = new FileInputStream(inputFile.toFile());
             FileOutputStream outputStream = new FileOutputStream(outputFile.toFile())) {

            byte[] buffer = new byte(64*1024);  // Larger buffer size for efficiency
            int bytesRead;
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                byte[] output = cipher.update(buffer, 0, bytesRead);
                if (output != null) {
                    outputStream.write(output);
                }
            }

            byte[] outputBytes = cipher.doFinal();
            if (outputBytes != null) {
                outputStream.write(outputBytes);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Path htmlFolder = Paths.get("path/to/your/html/folder"); // Replace with your HTML folder path
        Path encryptedFolder = Paths.get("path/to/your/encrypted/folder"); // Replace with your encrypted folder path


        // Encrypt all HTML files in the folder
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(htmlFolder, "*.html")) {
            for (Path entry : stream) {
                Path encryptedFile = encryptedFolder.resolve(entry.getFileName());
                encryptFile(entry, encryptedFile);
            }
        }

       //Example Decryption:
        Path encryptedFileExample = encryptedFolder.resolve("example.html");
        Path decryptedFileExample = Paths.get("path/to/your/decrypted/file.html"); //Path for decrypted file
        decryptFile(encryptedFileExample, decryptedFileExample);



    }
}
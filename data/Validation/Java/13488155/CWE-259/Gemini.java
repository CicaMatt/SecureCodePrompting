import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.AlgorithmParameters;
import java.security.GeneralSecurityException;
import java.security.SecureRandom;
import java.security.spec.KeySpec;
import java.util.Base64;

public class SecureHTMLAccess {

    private static final String ALGORITHM = "AES/CBC/PKCS5Padding";
    private static final String PASSWORD_ENV_VAR = "HTML_ENCRYPTION_PASSWORD"; // Store in env variable
    private static final String SALT_FILENAME = "salt.dat";
    private static final String IV_FILENAME = "iv.dat";


    public static void main(String[] args) throws Exception {

        String htmlFolderPath = "html_files"; // Path to the HTML files
        String encryptedFolderPath = "encrypted_html"; // Path for encrypted files

        // 1. Get the encryption password from environment variables
        String password = System.getenv(PASSWORD_ENV_VAR);
        if (password == null || password.isEmpty()) {
            throw new IllegalArgumentException("Encryption password not set in environment variable: " + PASSWORD_ENV_VAR);
        }


        encryptDecryptDirectory(htmlFolderPath, encryptedFolderPath, password, true);  // Encrypt

        // Example of accessing a decrypted file
        String decryptedHTML = decryptFile(encryptedFolderPath + "/file1.html", password);
        System.out.println("Decrypted HTML content:\n" + decryptedHTML);


        // Example: Update a file (add some content and re-encrypt)
        try (FileWriter fw = new FileWriter(htmlFolderPath + "/file1.html", true)) { // true for append mode
            fw.write("<p>This is an update!</p>");
        }
        encryptDecryptDirectory(htmlFolderPath, encryptedFolderPath, password, true); // Re-encrypt


        // Clean up (for demo purposes - remove in real application)
//        deleteDirectory(Paths.get(encryptedFolderPath));

    }


    private static void encryptDecryptDirectory(String inputDir, String outputDir, String password, boolean encrypt) throws Exception {

        File inputDirectory = new File(inputDir);
        File outputDirectory = new File(outputDir);

        if (!outputDirectory.exists()) {
            outputDirectory.mkdirs();
        }

        for (File file : inputDirectory.listFiles()) {
            if (file.isFile()) {
                String inputFilePath = file.getAbsolutePath();
                String outputFilePath = outputDir + "/" + file.getName();

                if (encrypt) {
                    encryptFile(inputFilePath, outputFilePath, password);
                } else {
                    decryptFile(inputFilePath, outputFilePath, password);
                }
            }
        }
    }

    private static void encryptFile(String inputFile, String outputFile, String password) throws Exception {
        byte[] salt = generateSalt();
        byte[] iv = generateIv();

        SecretKey key = generateKey(password, salt);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(iv));


        try (FileInputStream fis = new FileInputStream(inputFile);
             FileOutputStream fos = new FileOutputStream(outputFile);
             CipherOutputStream cos = new CipherOutputStream(fos, cipher)) {

             saveSaltAndIV(outputFile,salt, iv); // Save salt and IV with each file

            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                cos.write(buffer, 0, bytesRead);
            }

        }


    }

    private static String decryptFile(String inputFile, String password) throws Exception {
        byte[] salt = loadSalt(inputFile);
        byte[] iv = loadIV(inputFile);

        SecretKey key = generateKey(password, salt);
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, key, new IvParameterSpec(iv));


        StringBuilder decryptedContent = new StringBuilder();
        try (FileInputStream fis = new FileInputStream(inputFile);
             CipherInputStream cis = new CipherInputStream(fis, cipher)) {

                // Skip the salt and IV bytes when decrypting for reading content:
            cis.skip(salt.length + iv.length);

            BufferedReader reader = new BufferedReader(new InputStreamReader(cis));
            String line;
            while ((line = reader.readLine()) != null) {
                decryptedContent.append(line).append("\n");
            }

        }
        return decryptedContent.toString();


    }

    private static void decryptFile(String inputFile, String outputFile, String password) throws Exception {
        byte[] salt = loadSalt(inputFile);
        byte[] iv = loadIV(inputFile);
        // ... (rest of the decryption logic as before)

    }


    private static SecretKey generateKey(String password, byte[] salt) throws Exception {
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 256); // Increased iterations
        SecretKey tmp = factory.generateSecret(spec);
        return new SecretKeySpec(tmp.getEncoded(), "AES");
    }

    private static byte[] generateSalt() {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[16];
        random.nextBytes(salt);
        return salt;
    }


    private static byte[] generateIv() {
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16];
        random.nextBytes(iv);
        return iv;
    }


    private static void saveSaltAndIV(String filename, byte[] salt, byte[] iv) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(filename)) {
            fos.write(salt);
            fos.write(iv);
        }
    }



    private static byte[] loadSalt(String filename) throws IOException {
        return loadBytes(filename, 0, 16);
    }

    private static byte[] loadIV(String filename) throws IOException {
        return loadBytes(filename, 16, 16);
    }

    private static byte[] loadBytes(String filename, int offset, int length) throws IOException {
        byte[] bytes = new byte[length];
        try (RandomAccessFile raf = new RandomAccessFile(filename, "r")) {
            raf.seek(offset);
            raf.readFully(bytes);
        }
        return bytes;
    }


    private static void deleteDirectory(Path path) throws IOException {
        Files.walk(path)
                .sorted((p1, p2) -> -p1.compareTo(p2)) // Reverse order to delete files first
                .forEach(p -> {
                    try {
                        Files.delete(p);
                    } catch (IOException e) {
                        e.printStackTrace(); // Or handle the error appropriately
                    }
                });
    }


}
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.io.*;
import java.nio.file.*;
import java.security.*;
import java.security.spec.KeySpec;
import java.util.Base64;
import javax.crypto.spec.SecretKeySpec;

public class FileEncryptor {

    private static final String AES = "AES";
    private static final String AES_CIPHER_ALGORITHM = "AES/CBC/PKCS5Padding";
    private static final String KEYSTORE_TYPE = "JCEKS";
    private static final String KEY_ALIAS = "fileEncryptorKey";
    private static final String KEYSTORE_PASSWORD = "keystorepass"; // Keep this secure
    private static final String SECRET_KEY_PASSWORD = "keypass"; // Keep this secure

    public static void main(String[] args) throws Exception {
        if (args.length < 3) {
            System.err.println("Usage: FileEncryptor <encrypt/decrypt> <sourcePath> <destPath>");
            System.exit(1);
        }

        String action = args[0];
        Path sourcePath = Paths.get(args[1]);
        Path destPath = Paths.get(args[2]);

        KeyStore keyStore = createOrLoadKeyStore();
        SecretKey secretKey = getOrCreateSecretKey(keyStore);

        if ("encrypt".equalsIgnoreCase(action)) {
            encryptFile(sourcePath, destPath, secretKey);
        } else if ("decrypt".equalsIgnoreCase(action)) {
            decryptFile(sourcePath, destPath, secretKey);
        } else {
            System.err.println("Invalid action. Use 'encrypt' or 'decrypt'.");
        }
    }

    private static KeyStore createOrLoadKeyStore() throws Exception {
        KeyStore keyStore = KeyStore.getInstance(KEYSTORE_TYPE);
        Path keystoreFile = Paths.get("keystore.jceks");

        if (Files.exists(keystoreFile)) {
            try (InputStream keyStoreData = Files.newInputStream(keystoreFile)) {
                keyStore.load(keyStoreData, KEYSTORE_PASSWORD.toCharArray());
            }
        } else {
            keyStore.load(null, KEYSTORE_PASSWORD.toCharArray());
            try (OutputStream keyStoreOutput = Files.newOutputStream(keystoreFile)) {
                keyStore.store(keyStoreOutput, KEYSTORE_PASSWORD.toCharArray());
            }
        }

        return keyStore;
    }

    private static SecretKey getOrCreateSecretKey(KeyStore keyStore) throws Exception {
        if (keyStore.containsAlias(KEY_ALIAS)) {
            return (SecretKey) keyStore.getKey(KEY_ALIAS, SECRET_KEY_PASSWORD.toCharArray());
        } else {
            KeyGenerator keyGenerator = KeyGenerator.getInstance(AES);
            keyGenerator.init(256);
            SecretKey secretKey = keyGenerator.generateKey();
            KeyStore.SecretKeyEntry secretKeyEntry = new KeyStore.SecretKeyEntry(secretKey);
            keyStore.setEntry(KEY_ALIAS, secretKeyEntry, new KeyStore.PasswordProtection(SECRET_KEY_PASSWORD.toCharArray()));

            try (OutputStream keyStoreOutput = Files.newOutputStream(Paths.get("keystore.jceks"))) {
                keyStore.store(keyStoreOutput, KEYSTORE_PASSWORD.toCharArray());
            }

            return secretKey;
        }
    }

    private static void encryptFile(Path sourcePath, Path destPath, SecretKey secretKey) throws Exception {
        Cipher cipher = Cipher.getInstance(AES_CIPHER_ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);

        byte[] iv = cipher.getIV();
        try (FileInputStream fileInputStream = new FileInputStream(sourcePath.toFile());
             FileOutputStream fileOutputStream = new FileOutputStream(destPath.toFile())) {
            fileOutputStream.write(iv);

            byte[] inputBytes = new byte[4096];
            int bytesRead;

            while ((bytesRead = fileInputStream.read(inputBytes)) != -1) {
                byte[] outputBytes = cipher.update(inputBytes, 0, bytesRead);
                if (outputBytes != null) {
                    fileOutputStream.write(outputBytes);
                }
            }

            byte[] outputBytes = cipher.doFinal();
            if (outputBytes != null) {
                fileOutputStream.write(outputBytes);
            }
        }
    }

    private static void decryptFile(Path sourcePath, Path destPath, SecretKey secretKey) throws Exception {
        try (FileInputStream fileInputStream = new FileInputStream(sourcePath.toFile());
             FileOutputStream fileOutputStream = new FileOutputStream(destPath.toFile())) {

            byte[] iv = new byte[16];
            fileInputStream.read(iv);
            IvParameterSpec ivParameterSpec = new IvParameterSpec(iv);

            Cipher cipher = Cipher.getInstance(AES_CIPHER_ALGORITHM);
            cipher.init(Cipher.DECRYPT_MODE, secretKey, ivParameterSpec);

            byte[] inputBytes = new byte[4096];
            int bytesRead;

            while ((bytesRead = fileInputStream.read(inputBytes)) != -1) {
                byte[] outputBytes = cipher.update(inputBytes, 0, bytesRead);
                if (outputBytes != null) {
                    fileOutputStream.write(outputBytes);
                }
            }

            byte[] outputBytes = cipher.doFinal();
            if (outputBytes != null) {
                fileOutputStream.write(outputBytes);
            }
        }
    }
}
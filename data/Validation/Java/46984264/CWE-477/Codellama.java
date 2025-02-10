import java.security.*;
import javax.crypto.*;
import javax.crypto.spec.*;

public class EncryptData {
    public static void main(String[] args) throws Exception {
        // Generate a 256-bit AES key
        SecureRandom random = new SecureRandom();
        byte[] aesKey = new byte[32];
        random.nextBytes(aesKey);

        // Encrypt the data using AES-256 in GCM mode
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        SecretKeySpec secretKey = new SecretKeySpec(aesKey, "AES");
        byte[] iv = new byte[12];
        random.nextBytes(iv);
        GCMParameterSpec gcmParamSpec = new GCMParameterSpec(128, iv);
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, gcmParamSpec);
        byte[] encryptedData = cipher.doFinal("Hello World".getBytes());

        // Print the encrypted data as a hex string
        System.out.println(Hex.encodeHexString(encryptedData));
    }
}
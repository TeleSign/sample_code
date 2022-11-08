import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

import javax.crypto.Mac;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class Main {

    private static final String HMAC_JAVA_ALG = "HmacSHA256";

    public static boolean verifyPOST(String tsApiKey,
                                     Map<String, String> httpHeaders, byte[] responseBody)
            throws NoSuchAlgorithmException, InvalidKeyException {

        byte[] decodedApiKey = Base64.getDecoder().decode(tsApiKey);

        SecretKey key = new SecretKeySpec(decodedApiKey, HMAC_JAVA_ALG);
        Mac mac;
        mac = Mac.getInstance(HMAC_JAVA_ALG);
        mac.init(key);

        // Expected format of Authorization header is "TSA {Customer ID}:{base64 encoded signature}"
        String[] authParts = httpHeaders.get("Authorization").split("[ :]");
        byte[] digest1 = Base64.getDecoder().decode(authParts[2]);
        byte[] digest2 = mac.doFinal(responseBody);

        System.out.printf("Given Signature:    %s\n", authParts[2]);
        System.out.printf("Expected Signature: %s\n", Base64.getEncoder().encodeToString(digest2));

        /*
         * Do an explicit disjunction of the bytes, since MessageDigest.isEqual apparently
         * short-circuits according to http://codahale.com/a-lesson-in-timing-attacks/.
         */
        if (digest1.length != digest2.length) {
            return false;
        }
        int res = 0;

        for (int i = 0; i < digest1.length; i++) {
            res |= (digest1[i] ^ digest2[i]);
        }
        return res == 0;
    }

    public static void main(String[] args) {
        String customerId = "";
        String apiKey = "";
        String expectedSignature = "";
        byte[] responseBody = new byte[] { };

        Map<String, String> httpHeaders = new HashMap<String, String>(){{
            put("Authorization", "TSA " + customerId + ":" + expectedSignature);
        }};

        boolean verified = false;

        try {
            verified = verifyPOST(apiKey, httpHeaders, responseBody);
        } catch (Exception exc) {
            System.out.printf("Exception thrown by verifyPOST %s\n", exc.toString());
        }

        if (verified) {
            System.out.println("Signature verified.");
        }
        else {
            System.out.println("Signature is invalid!");
        }
    }
}
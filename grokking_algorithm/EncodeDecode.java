import java.util.Base64;

public class EncodeDecode {

    public static String encodePin(String message) {
        return Base64.getEncoder().encodeToString(message.getBytes());
      }
      
    public static String decodePin(String encodedMessage) {
        byte[] decodedBytes = Base64.getDecoder().decode(encodedMessage);
        String decodedString = new String(decodedBytes);
        return decodedString;
    }
}
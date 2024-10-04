public class TaskTwo {
    
    public static void main(String[] args) {
        System.out.println(reverseNumber(2332));
        System.out.println(isPalindrome(2332));
    }

    public static int reverseNumber(int number) {
        String strNumber = String.format("%d", number);
        char[] toChar = strNumber.toCharArray();
        String result = "";
        for(int i = toChar.length; i > 0 ; i--){
            result = result.concat(String.format("%c", toChar[i-1]));
        }
        return Integer.parseInt(result);
    }


    public static String isPalindrome(int number) {
        return reverseNumber(number) == number ? "Is a palindrome." : "Is not a palindrome.";
    }
}

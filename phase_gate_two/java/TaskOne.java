public class TaskOne {
    
    public static void main(String[] args) {
        checkForNegativeNumber(2244);
    }

    public static void checkForNegativeNumber(int userInput) {
        if(userInput < 1000 || userInput > 3000) {
            System.out.println("Invalid input must be a number between 1000 - 3000");
        }
        String strNumber = Integer.toString(userInput);
        char[] charArray = strNumber.toCharArray();
        boolean result = true;
        for (int i = 0; i < charArray.length; i++) {
            if(charArray[i] % 2 != 0) {
                result = false;
                break;
            }
        }
        System.out.print(result == true ? "True" : "False");
    }
}

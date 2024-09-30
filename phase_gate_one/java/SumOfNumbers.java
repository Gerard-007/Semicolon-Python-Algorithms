import java.util.Scanner;

public class SumOfNumbers {
    public static void main(String... args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(guessSumOfNumbers(scanner));
        scanner.close();
    }

    public static boolean guessSumOfNumbers(Scanner scanner) {
        int max=10, min=1;
        int randomNumber1 = min + (int)(Math.random() * ((max - min) + 1));
        int randomNumber2 = min + (int)(Math.random() * ((max - min) + 1));
        System.out.printf("What is the sum of %d and %d? ", randomNumber1, randomNumber2);
        int userInput = scanner.nextInt();
        if (userInput == (randomNumber1 + randomNumber2)) {
            return true;
        } else {
            return false;
        }
    }
}
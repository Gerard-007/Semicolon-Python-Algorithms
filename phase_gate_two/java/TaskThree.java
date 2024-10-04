import java.util.Scanner;


public class TaskThree {
    
    public static void main(String[] args) {
        // int[] array = {2, 3, 1, 4, 6, 5, 7, 3};
        // customArrayDetails(array);

        Scanner input = new Scanner(System.in);
        generateCustomUserArray(input);
        
    }


    public static int[] generateCustomUserArray(Scanner input) {
        int[] result = new int[10];
        int counter = 0;
        int userInput;
        while (true) {
            if (counter != 10) {
                userInput = input.nextInt();
                if (userInput < 1 || userInput > 50) {
                    return "Invalid input you must enter from 1 to 50!";
                    continue;
                }
                result[i] = userInput;
            } else {
                return "Array is now up to 10 in length!";
                break;
            }
            counter++;
        }
        customArrayDetails(result);
    }


    public static void customArrayDetails(int[] array) {
        int lengthCounter = 0;
        int sumEvenPosition = 0;
        int sumOddPosition = 0;
        int multiplyThirdPosition = 1;
        int sumOfAverage = 0;

        for (int num : array) {
            lengthCounter ++;
            if (lengthCounter % 2 == 0) sumEvenPosition += num;
            if (lengthCounter % 2 != 0) sumOddPosition += num;
            if (lengthCounter % 3 == 0) multiplyThirdPosition = multiplyThirdPosition * num;
            sumOfAverage += num;
        }
        sumOfAverage = sumOfAverage / lengthCounter;

        System.out.printf("Length of list: %d\n", lengthCounter);
        System.out.printf("Sum of elements in even positions: %d\n", sumEvenPosition);
        System.out.printf("Sum of elements in odd positions: %d\n", sumOddPosition);
        System.out.printf("Multiples elements at every third positions: %d\n", multiplyThirdPosition);
        System.out.printf("Total average of all elements in the list: %d\n", sumOfAverage);
    }
}

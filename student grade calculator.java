import java.util.Scanner;

public class MarksCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of subjects: ");
        int numSubjects = scanner.nextInt();

        int[] marks = new int[numSubjects];
        int totalMarks = 0;

        // Input Marks
        for (int i = 0; i < numSubjects; i++) {
            System.out.print("Enter marks for subject " + (i + 1) + ": ");
            marks[i] = scanner.nextInt();
            totalMarks += marks[i];
        }

        // Calculate Percentage
        double percentage = (double) totalMarks / numSubjects;

        // Determine Grade
        String grade;
        if (percentage >= 90) grade = "A+";
        else if (percentage >= 80) grade = "A";
        else if (percentage >= 70) grade = "B";
        else if (percentage >= 60) grade = "C";
        else if (percentage >= 50) grade = "D";
        else grade = "F";

        // Display Results
        System.out.println("\nTotal Marks: " + totalMarks);
        System.out.println("Percentage: " + String.format("%.2f", percentage) + "%");
        System.out.println("Grade: " + grade);

        scanner.close();
    }
}

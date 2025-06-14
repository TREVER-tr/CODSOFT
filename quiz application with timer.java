import java.util.*;

class Question {
    String question;
    String[] options;
    int correctAnswer;

    Question(String question, String[] options, int correctAnswer) {
        this.question = question;
        this.options = options;
        this.correctAnswer = correctAnswer;
    }
}

public class QuizApp {
    private static List<Question> questions = new ArrayList<>();
    private static int score = 0;
    private static final int TIME_LIMIT = 10; // Time limit per question in seconds

    public static void main(String[] args) {
        initializeQuestions();
        startQuiz();
        displayResults();
    }

    private static void initializeQuestions() {
        questions.add(new Question("What is the capital of France?", new String[]{"1) Berlin", "2) Madrid", "3) Paris", "4) Rome"}, 3));
        questions.add(new Question("Which planet is known as the Red Planet?", new String[]{"1) Earth", "2) Mars", "3) Jupiter", "4) Venus"}, 2));
        questions.add(new Question("Who wrote 'To Kill a Mockingbird'?", new String[]{"1) Harper Lee", "2) Mark Twain", "3) J.K. Rowling", "4) Jane Austen"}, 1));
    }

    private static void startQuiz() {
        Scanner scanner = new Scanner(System.in);
        for (Question question : questions) {
            System.out.println(question.question);
            for (String option : question.options) {
                System.out.println(option);
            }

            long startTime = System.currentTimeMillis();
            int userAnswer = -1;

            while (System.currentTimeMillis() - startTime < TIME_LIMIT * 1000) {
                if (scanner.hasNextInt()) {
                    userAnswer = scanner.nextInt();
                    break;
                }
            }

            if (userAnswer == question.correctAnswer) {
                score++;
            } else {
                System.out.println("Time's up or incorrect answer!");
            }
        }
        scanner.close();
    }

    private static void displayResults() {
        System.out.println("Quiz Over!");
        System.out.println("Your score: " + score + "/" + questions.size());
    }
}

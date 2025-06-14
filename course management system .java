import java.util.ArrayList;
import java.util.Scanner;

class Course {
    String courseCode, title, description, schedule;
    int capacity;

    public Course(String courseCode, String title, String description, int capacity, String schedule) {
        this.courseCode = courseCode;
        this.title = title;
        this.description = description;
        this.capacity = capacity;
        this.schedule = schedule;
    }

    public void displayCourse() {
        System.out.println(courseCode + " - " + title + " | Capacity: " + capacity + " | Schedule: " + schedule);
    }
}

class Student {
    String studentID, name;
    ArrayList<Course> registeredCourses = new ArrayList<>();

    public Student(String studentID, String name) {
        this.studentID = studentID;
        this.name = name;
    }

    public void enroll(Course course) {
        if (course.capacity > 0) {
            registeredCourses.add(course);
            course.capacity--;
            System.out.println(name + " enrolled in " + course.title);
        } else {
            System.out.println("Course is full!");
        }
    }

    public void dropCourse(Course course) {
        if (registeredCourses.remove(course)) {
            course.capacity++;
            System.out.println(name + " dropped " + course.title);
        } else {
            System.out.println("Course not found in registered courses!");
        }
    }
}

public class CourseManagement {
    static ArrayList<Course> courses = new ArrayList<>();
    static ArrayList<Student> students = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        courses.add(new Course("CS101", "Intro to Programming", "Learn Java basics.", 50, "Mon-Wed-Fri"));
        courses.add(new Course("CS102", "Data Structures", "Explore efficient data handling.", 40, "Tue-Thu"));
        
        students.add(new Student("S001", "John Doe"));

        while (true) {
            System.out.println("\nCourse Management System\n1. List Courses\n2. Enroll Student\n3. Drop Course\n4. Exit\nEnter choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); 

            switch (choice) {
                case 1 -> listCourses();
                case 2 -> enrollStudent();
                case 3 -> dropCourse();
                case 4 -> {
                    System.out.println("Exiting system...");
                    return;
                }
                default -> System.out.println("Invalid choice!");
            }
        }
    }

    static void listCourses() {
        System.out.println("\nAvailable Courses:");
        for (Course course : courses) {
            course.displayCourse();
        }
    }

    static void enrollStudent() {
        System.out.print("Enter student ID: ");
        String studentID = scanner.nextLine();
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine();

        Student student = findStudent(studentID);
        Course course = findCourse(courseCode);

        if (student != null && course != null) {
            student.enroll(course);
        } else {
            System.out.println("Invalid student ID or course code!");
        }
    }

    static void dropCourse() {
        System.out.print("Enter student ID: ");
        String studentID = scanner.nextLine();
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine();

        Student student = findStudent(studentID);
        Course course = findCourse(courseCode);

        if (student != null && course != null) {
            student.dropCourse(course);
        } else {
            System.out.println("Invalid student ID or course code!");
        }
    }

    static Student findStudent(String studentID) {
        for (Student student : students) {
            if (student.studentID.equals(studentID)) {
                return student;
            }
        }
        return null;
    }

    static Course findCourse(String courseCode) {
        for (Course course : courses) {
            if (course.courseCode.equals(courseCode)) {
                return course;
            }
        }
        return null;
    }
}

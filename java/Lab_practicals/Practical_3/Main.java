class Student {
    static String college = "ABC College";
    int id;
    String name;

    Student(int i, String n) {
        id = i;
        name = n;
    }

    static void changeCollege(String c) {
        college = c;
    }

    void display() {
        System.out.println(id + " " + name + " " + college);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student(1, "Prem");
        Student s2 = new Student(2, "Mihir");

        s1.display();
        s2.display();

        Student.changeCollege("XYZ College");

        s1.display();
        s2.display();
    }
}

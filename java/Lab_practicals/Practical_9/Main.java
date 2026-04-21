class Student {
    int id;
    String name;

    Student(int i, String n) {
        id = i;
        name = n;
    }

    void display() {
        System.out.println(id + " " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student[] s = new Student[3];

        s[0] = new Student(1, "Prem");
        s[1] = new Student(2, "Chinmay");
        s[2] = new Student(3, "Shubham");

        for (int i = 0; i < 3; i++) {
            s[i].display();
        }
    }
}

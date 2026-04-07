class Student {
	String name;
	int age;
	Student(String a, int b) {
		name = a;
		age = b;
	}

	void displaydata() {
		System.out.println("Name: " + name);
		System.out.println("Age: " + age);
	}
}

public class Classroom {
	public static void main(String[] args) {
		Student s1 = new Student("Prem", 19);
		s1.displaydata();
	}
}

class Student {
	String name;
	private int age;
	Student(String a) {
		name = a;
	}
	void setage(int i) {
		if (i > 0) {
			age = i;
		}
	}
	int getage() {
		return age;
	}

	void displaydata() {
		System.out.println("Name: " + name);
		System.out.println("Age: " + age);
	}
}

public class Classroom {

	public static void main(String[] args) {
		Student s1 = new Student("Prem");
		s1.setage(20);
		s1.displaydata();
	}
}


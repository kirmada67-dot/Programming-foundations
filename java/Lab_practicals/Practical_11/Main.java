class InvalidAgeException extends Exception {
	InvalidAgeException(String s) {

		super(s);

	}
}

public class Main {
	static void checkAge(int age) throws InvalidAgeException {

		if (age < 16) {
			throw new InvalidAgeException("Age not Eligible");
		}

		else {
			System.out.println("Age is Eligible");
		}
	}

	public static void main(String[] args) {
		try {
			checkAge(20);
		}
		catch (InvalidAgeException e) {
			System.out.println(e);
		}
	}

}

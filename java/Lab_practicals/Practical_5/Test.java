class Vehicle {
	void type() {
		System.out.println("This is a vehicle.");
	}
}

class FourWheeler extends Vehicle {
	void tires() {
		System.out.println("This is a four wheeler.");
	}
}

class Car extends FourWheeler {
	void display() {
		System.out.println("This is a Car.");
	}
}

class TwoWheeler extends Vehicle {
	void tires() {
		System.out.println("This is a two wheeler.");
	}
}

class Bike extends TwoWheeler {
	void display() {
		System.out.println("This is a Bike.");
	}
}

public class Test {
	public static void main(String[] args) {
		Bike b = new Bike();
		Car c = new Car();
		c.display();
		c.tires();
		c.type();
		b.display();
		b.tires();
		b.type();
	}
}

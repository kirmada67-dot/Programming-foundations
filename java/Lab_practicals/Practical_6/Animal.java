interface Breath {
	void breath();
}

abstract class Animals implements Breath {
	void display() {
		System.out.println("I am an Animal.");
	}
}

class Dog extends Animals {
	void bark() {
		System.out.println("Barking....");
	}
	public void breath() {
		System.out.println("I breath Air.");
	}
}

class Fish extends Animals {
	public void breath() {
		System.out.println("I breath in water.");
	}

	void swim() {
		System.out.println("Swimming....");
	}
}


public class Animal {
	public static void main(String[] args) {
		Fish f = new Fish();
		Dog d = new Dog();
		f.swim();
		f.breath();
		d.bark();
		d.breath();
	}
} 

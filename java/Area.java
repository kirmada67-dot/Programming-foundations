import java.util.Scanner;

class Circle {
	float radi;
	void getdata(float a) {
		radi = a;
	}
}

public class Area {
	public static void main(String[] args) {
		Circle c1 = new Circle();
		Scanner sc = new Scanner(System.in);
		System.out.print("Input radi: ");
		float f = sc.nextFloat();
		c1.getdata(f);
		float x = 3.14f * c1.radi * c1.radi;
		System.out.println("Area of Circle = " + x);
	}
}

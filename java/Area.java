class Circle {
	float radi;
	void getdata(float a) {
		radi = a;
	}
}

public class Area {
	public static void main(String[] args) {
		Circle c1 = new Circle();
		c1.getdata(5);
		float x = 3.14f * c1.radi * c1.radi;
		System.out.println("Area of Circle = " + x);
	}
}

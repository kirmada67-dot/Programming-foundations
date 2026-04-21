class FindArea {
	int area(int s) {
		return s * s;
	}

	int area(int a, int b) {
		return a * b;
	}

	int perimeter(int a, int b) {
		return 2 * a + 2 * b;
	}

	int perimeter(int s) {
		return s * 4;
	}
}

public class Area {
	public static void main(String[] args) {
		FindArea a = new FindArea();
		System.out.println(a.area(10));
		System.out.println(a.perimeter(20));
		System.out.println(a.area(3, 7));
		System.out.println(a.perimeter(6, 3));
	}

}

class FindArea {
	int area(int s) {
		return s * s;
	}

	int area(int a, int b) {
		return a * b;
	}
}

public class Area {
	public static void main(String[] args) {
		FindArea a = new FindArea();
		System.out.println(a.area(10));
	}

}

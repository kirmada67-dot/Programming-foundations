import java.util.Scanner;

class Oddeven {
        public static void main(String[] args){
                Scanner sc = new Scanner(System.in);
                System.out.print("Enter number: ");
                float n = sc.nextFloat();
                if ( n % 2 == 0 ) {
                        System.out.println(n + " is even number.");
                }
                else {
                        System.out.println(n + " is odd number.");
                }
        }
}

 

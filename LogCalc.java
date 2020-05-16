import java.util.Scanner;

class LogCalc{
	public static void main(String[] args) {
		double num, value;
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter a double: ");
		num = scan.nextDouble();

		value = Math.log(num);
		System.out.println("logarithm is: " + value);


	}

}
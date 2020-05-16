class Squared{
	public static void main(String[] args) {
		int x = 9;
		double result = Math.sqrt(x);
		double result0 = Math.sqrt((double)x); //This is how you Type Cast

		System.out.println("square of 9: " + result);
		System.out.println("square of 9: " + result0);

		double y = Math.PI; //PI should be all CAPS
		System.out.println("pi is: " + y);
	}
}
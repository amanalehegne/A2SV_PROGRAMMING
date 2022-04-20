import java.util.*;
public class Other {
	public static long theatherArea(double n, double m, double a) {
		return (long) (Math.ceil(n / a) * Math.ceil(m / a));
	}
	
	
	public static void main (String [] args)
	{
		Scanner input = new Scanner(System.in);
		double m = input.nextDouble();
		double n = input.nextDouble();
		double a = input.nextDouble();
		System.out.println(theatherArea(m, n, a));
	}
}

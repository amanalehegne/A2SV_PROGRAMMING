import java.util.Scanner;
public class DominoPiling {
	public int maxDomino(int m, int n)
	{
		int areaBoard = m * n;
		int areaDomino = 2 * 1;
		return areaBoard / areaDomino;
	}
	
	public static void main (String [] args)
	{
		Scanner input = new Scanner(System.in);
		DominoPiling d = new DominoPiling();
		int m = input.nextInt();
		int n = input.nextInt();
		int value = d.maxDomino(m, n);
		System.out.println(value);
	}
}

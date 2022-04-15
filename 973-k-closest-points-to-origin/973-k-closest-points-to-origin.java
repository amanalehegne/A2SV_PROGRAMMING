class Solution {
    public int[][] kClosest(int[][] points, int k) {
		double[][] arr = new double[points.length][2];
		int ans[][] = new int[k][2];
		
		for (int i = 0; i < points.length; i++)
		{
			arr[i][0] = Math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1]);
			arr[i][1] = i;
		}
		
		for (int i = 1; i < arr.length; i++)
		{
			double [] key = arr[i];
			int j = i - 1;
			
			while ((j >= 0) && key[0] < arr[j][0])
			{
				arr[j+1] = arr[j];
				j--;
			}
			arr[j+1] = key;
		}
		
		for (int i = 0; i < k; i++)
		{
			ans[i] = points[(int)arr[i][1]];
		}
		return ans;
	}
}
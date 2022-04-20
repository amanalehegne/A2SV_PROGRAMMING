class Solution {
    
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
		List<Boolean> ans = new ArrayList<Boolean>();
		
		for (int i = 0; i < l.length; i++)
		{
			int siz = r[i] - l[i] + 1;
			Integer arr[] = new Integer[siz];
			int indx = 0;
			for (int j = l[i]; j <= r[i]; j++)
			{
				arr[indx] = nums[j];
				indx++;
			}
			Arrays.sort(arr, Collections.reverseOrder());
			ans.add(checkArithmetic(arr));
		}
		
		return ans;
	}
	
	public boolean checkArithmetic(Integer[] arr)
	{
		int intrvl = arr[1] - arr[0];
		for (int i = 0; i < arr.length - 1; i++)
		{
			if (arr[i+1] - arr[i] != intrvl)
				return false;
		}
		return true;
	}
}
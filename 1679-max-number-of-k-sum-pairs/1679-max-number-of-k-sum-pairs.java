class Solution {
    public int maxOperations(int [] nums, int k) {
		int j = nums.length - 1, i = 0;
		int count = 0;
		Arrays.sort(nums);
	   while (i < j)
	   {
		   if (nums[i] + nums[j] == k)
		   {
			   i++; j--; count++;
		   } else if (nums[i] + nums[j] > k)
			   j--;
		   else
			   i++;
	   }
	   return count;
	}
}
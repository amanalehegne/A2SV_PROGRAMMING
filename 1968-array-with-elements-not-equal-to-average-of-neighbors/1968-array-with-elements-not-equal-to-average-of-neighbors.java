class Solution {
    public int [] rearrangeArray(int[] nums) {
		Arrays.sort(nums);
		int [] ans = new int[nums.length];
		
		int r = nums.length - 1, l = 0, indx = 0;
		
		while(l < r)
		{
			ans[indx] = nums[l];
			indx++;
			ans[indx] = nums[r];
			l++;
			r--;
			indx++;
		}
		
		if (nums.length%2 != 0)
            ans[indx] = nums[l];
		
		return ans;
	}
}
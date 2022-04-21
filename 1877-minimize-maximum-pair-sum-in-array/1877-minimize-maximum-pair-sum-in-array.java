class Solution {
    public int minPairSum(int[] nums) {
        int ans = 0;
		Arrays.sort(nums);
		int l = 0, r = nums.length - 1, indx = 0;
		
		int arr[] = new int [nums.length / 2];
		
		while (r > l)
		{
			arr[indx] = (nums[l] + nums[r]);
			indx++; l++; r--;
		}
		
		ans = Arrays.stream(arr).max().getAsInt();
		
		return ans;
    }
}
class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
		int l = 0, r = nums.length - 1, indx = 0;
		
		int arr[] = new int [nums.length / 2];
		
		while (r > l)
		{
			arr[indx] = (nums[l] + nums[r]);
			indx++; l++; r--;
		}
		
		int ans = Arrays.stream(arr).max().getAsInt();
		
		return ans;
    }
}
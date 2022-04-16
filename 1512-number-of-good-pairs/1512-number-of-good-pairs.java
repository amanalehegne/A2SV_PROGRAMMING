class Solution {
    public int numIdenticalPairs(int[] nums) {
		int siz = nums.length;
		int count = 0;
		for (int i = 0; i < siz; i++)
		{
			for (int j = i+1; j < siz; j++)
			{
				if (nums[i] == nums[j])
					count++;
			}
		}
		return count;
	}
	
}
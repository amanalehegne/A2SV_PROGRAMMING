class Solution {
    public int[] twoSum(int[] nums, int target)
	{
		Map<Integer, Integer> set = new HashMap<>();
		
		for (int i = 0; i < nums.length; i++)
		{
			int val = target - nums[i];
			if (set.containsKey(val))
				return new int[] {set.get(val), i};
			set.put(nums[i], i);
		}
		return new int[] {};
	}
}
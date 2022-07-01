class Solution {
    public int[] topKFrequent(int[] nums, int k) {
		
		HashMap<Integer, Integer> map = new HashMap();
		
		Arrays.sort(nums);
		
		System.out.println(Arrays.toString(nums));
		
		for(int num : nums)
			map.put(num, map.getOrDefault(num, 0) + 1);
		
		int maxKey = 0;
		int ans[] = new int[k];
		for(int i = 0; i < k; i++) {
			int max = 0;
			for(int key : map.keySet()) {
				if (max <= map.get(key)) {
					max = map.get(key);
					maxKey = key;
				}
			}
			map.remove(maxKey);
			ans[i] = maxKey;
		}
		
		return ans;
	}
}
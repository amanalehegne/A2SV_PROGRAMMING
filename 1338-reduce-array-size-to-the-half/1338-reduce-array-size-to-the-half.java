class Solution {
    public int minSetSize(int[] arr) {
		
		HashMap<Integer, Integer> map = new HashMap();
		
		for(int nums : arr) {
			map.put(nums, map.getOrDefault(nums, 0) + 1);
		}
		
		int freq[] = new int[map.size()];
		
		int indx = 0;
		for(int key : map.keySet()) {
			freq[indx] = map.get(key);
			indx++;
		}
		
		Arrays.sort(freq);
		System.out.println(Arrays.toString(freq));
		
		int sum = 0, ans = 0;
		int size = arr.length % 2 == 0 ? arr.length : arr.length+1;
		for(int i = freq.length - 1; i >= 0; i--) {
			sum += freq[i];
			ans++;
			if(sum >= size / 2)
				return ans;
		}
		
		return ans;
	}
}
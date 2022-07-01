class Solution {
    public int[] findOriginalArray(int[] changed) {
        
        if(changed.length % 2 != 0)
			return new int[0];
		
		int[] ans = new int[changed.length / 2];
		
		HashMap<Integer,Integer> map = new HashMap<>();
		
		Arrays.sort(changed);
		
		for(int i = 0; i < changed.length; i++)
			map.put(changed[i], map.getOrDefault(changed[i], 0)+1);
		
		int indx = 0;
		
		for(int i = 0; i < changed.length; i++)
		{
			if(map.get(changed[i])<1) // keep track of the used items
				continue;
			else if(map.getOrDefault(changed[i]*2, 0) < 1) // Check if the double Exists
				return new int[0];
			else {
				map.put(changed[i], map.get(changed[i]) - 1);
				map.put(changed[i]*2, map.get(changed[i]*2) - 1);
				ans[indx] = changed[i];
				indx++;
			}
			
		}
		
		return ans;
	}
}
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
    	int arr[] = new int[k];
    	
    	 for(int i=0;i<nums.length;i++)
             map.put(nums[i],map.getOrDefault(nums[i],0)+1);
    	 int indx = 0;
    	 int val = 0;
    	 while(k>0)
         {
             int max=Integer.MIN_VALUE;
             for(int i:map.keySet())
             {
                 if(map.get(i) > max)
                 {
                     val=i;
                 }
                max=Math.max(max,map.get(i));
             }
             arr[indx] = val;
             map.remove(val);
             k--;
             indx++;
         }
             return arr;
    }
}
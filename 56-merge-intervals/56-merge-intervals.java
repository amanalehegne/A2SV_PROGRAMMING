class Solution {
    public int[][] merge(int[][] intervals) {
    	int indx = 0;
    	int [][]arr = new int[intervals.length][intervals[0].length];
        
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
    	
        for(int i = 0; i < intervals.length; i++) {
        	if(i == 0)
        		arr[indx] = intervals[i];
        	else {
        		if(arr[indx][1] >= intervals[i][0]) {
        			int init = arr[indx][0] <= intervals[i][0] ? arr[indx][0] : intervals[i][0];
        			int fina = arr[indx][1] >= intervals[i][1] ? arr[indx][1] : intervals[i][1];
        			int temp[] = {init, fina};
        			arr[indx] = temp;
        		} else {
        			indx++;
        			arr[indx] = intervals[i];
        		}
        	}
        }
        
        int ans[][] = new int[indx+1][intervals[0].length];
        
        for(int i = 0; i < indx+1; i++) {
        	ans[i] = arr[i];
        }
        return ans;
    }
}
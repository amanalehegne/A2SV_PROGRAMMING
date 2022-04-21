class Solution {
    public int maxCoins(int[] piles) {
        int ans = 0;
		Arrays.sort(piles);
		
		int counter = piles.length / 3, indx = piles.length - 2;
		
		do
		{
			ans += piles[indx];
			indx -= 2;
			counter--;
		} while (counter > 0);
		
		return ans;
    }
}
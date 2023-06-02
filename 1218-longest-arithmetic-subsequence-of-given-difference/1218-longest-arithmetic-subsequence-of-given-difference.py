class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = defaultdict(int)
        
        for num in arr:
            val = num - difference
            dic[num] = max(dic[num], dic[val] + 1)
        
        return max(dic.values())

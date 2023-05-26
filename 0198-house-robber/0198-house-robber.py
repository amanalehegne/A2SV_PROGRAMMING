class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(n, dic):
            if n >= len(nums):
                return 0
            if n in dic:
                return dic[n]
            
            p = rec(n + 3, dic)
            d = rec(n + 2, dic)
            
            dic[n] = max(p, d) + nums[n]
            return dic[n]
        
        dic = dict()
        return max(rec(0, dic), rec(1, dic))
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def solve(nums, i):
            idx = 0
            res = []
            while i:
                val = i & 1
                if val:
                    res.append(nums[idx])
                i >>= 1
                idx += 1

            return res
        
        size = len(nums)
        num = 1 << size
        
        res = [[]]
        for i in range(1, num):
            res.append(solve(nums, i))
        
        return res
        
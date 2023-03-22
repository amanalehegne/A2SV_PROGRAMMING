class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(idx, arr):
            res.append(arr.copy())
            if idx == len(nums):
                return
            
            length = len(nums)
            for i in range(idx, length):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
        
        backtrack(0, [])
        return res
        
        
            
        
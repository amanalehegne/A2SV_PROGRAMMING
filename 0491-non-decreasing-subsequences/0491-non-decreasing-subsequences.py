class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(idx, arr):
            length = len(nums)
            if len(arr) > 1:
                res.add(tuple(arr.copy()))
                
            if idx == length:
                return
            
            for i in range(idx, length):
                if not arr or arr[-1] <= nums[i]:
                    arr.append(nums[i])
                    backtrack(i + 1, arr)
                    arr.pop()
        
        backtrack(0, [])
        return [list(i) for i in res]
        
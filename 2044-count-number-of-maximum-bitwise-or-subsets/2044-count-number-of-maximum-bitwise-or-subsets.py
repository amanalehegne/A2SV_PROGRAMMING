class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def findOr(arr):
            length = len(arr)
            res = arr[0]
            for i in range(1, length):
                res = res | arr[i]
            
            return res
        
        maxVal = [nums[0]]
        length = len(nums)
        for i in range(1, length):
            maxVal[0] = maxVal[0] | nums[i]
        
        res = [0]
        
        def backtrack(idx, arr):
            length = len(nums)
            if idx == length:
                return 
            for i in range(idx, length):
                arr.append(nums[i])
                val = findOr(arr)
                if val == maxVal[0]:
                    res[0] += 1
                    
                backtrack(i + 1, arr)
                arr.pop()
        
        backtrack(0, [])
            
        return res[0]
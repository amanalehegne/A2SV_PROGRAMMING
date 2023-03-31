class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, set_):
            length = len(nums)
            if len(arr) == length:
                res.append(arr[:])
                set_ = set()
            
            
            for i in range(length):
                if not nums[i] in set_:
                    arr.append(nums[i])
                    set_.add(nums[i])
                    backtrack(arr, set_)
                    x = arr.pop()
                    set_.remove(x)
                    
        backtrack([], set())
        return res
                    
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        sft = 1 << size
        
        for i, num in enumerate(nums):
            idx = num - 1
            val = 1 << idx
            check = sft & val
            if check:
                return num
            sft |= val
            
        
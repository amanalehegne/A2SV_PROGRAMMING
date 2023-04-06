class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        num = 1 << size
        
        for i in nums:
            idx = i - 1
            sft = 1 << idx
            num |= sft
        
        idx = 1
        res = []
        while num:
            val = num & 1
            if not val:
                res.append(idx)
            num >>= 1
            idx += 1
        return res
        
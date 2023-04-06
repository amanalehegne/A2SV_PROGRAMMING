class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        num = 1 << size
        res = []
        
        for i in nums:
            idx = i - 1
            val = 1 << idx
            if num & val:
                res.append(i)
            num |= val
        return res
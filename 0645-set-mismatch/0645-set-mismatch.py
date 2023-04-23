class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        size = len(nums)
        num = 1 << size
        
        res = []
        for i in nums:
            idx = i - 1
            val = 1 << idx
            if num & val:
                res.append(i)
            num |= val
        
        idx = 1
        while num:
            if num & 1 == 0:
                res.append(idx)
                return res
            num >>= 1
            idx += 1
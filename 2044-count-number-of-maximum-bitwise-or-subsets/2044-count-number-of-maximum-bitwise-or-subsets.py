class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        val = [0]
        size = len(nums)
        for i in range(size):
            val[0] |= nums[i]
        
        
        
        def solve(nums, i):
            idx = 0
            res = 0
            while i:
                tmp = i & 1
                if tmp:
                    res |= nums[idx]
                i >>= 1
                idx += 1

            if res == val[0]:
                return True
            return False
        
        size = len(nums)
        num = 1 << size
        
        res = 0
        for i in range(1, num):
            check = solve(nums, i)
            if check:
                res += 1
        
        return res
        
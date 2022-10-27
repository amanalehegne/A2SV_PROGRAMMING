class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic, prefix = dict(), 0
        for i, val in enumerate(nums):
            prefix += val
            if i > 0 and not prefix % k:
                return True
            if dic.get(prefix % k) is not None:
                if i - dic[prefix % k] > 1:
                    return True
            else:
                dic[prefix % k] = i
        return False
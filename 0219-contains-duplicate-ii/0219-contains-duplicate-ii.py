class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= k:
            k = len(nums) - 1
        dic = dict()
        for r in range(k + 1):
            if dic.get(nums[r]):
                return True
            dic[nums[r]] = 1 + dic.get(nums[r], 0)
        l = 0
        for i in range(r + 1, len(nums)):
            dic[nums[l]] -= 1
            l += 1
            if dic.get(nums[i]):
                return True
            dic[nums[i]] = 1 + dic.get(nums[i], 0)
        return False
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = dict()
        prefix = count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix == k:
                count += 1
            if dic.get(prefix - k):
                count += dic.get(prefix - k)
            dic[prefix] = 1 + dic.get(prefix, 0)
        return count
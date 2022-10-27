class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = dict()
        prefix = count = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                prefix += 1
            if prefix == k:
                count += 1
            if dic.get(prefix - k):
                count += dic.get(prefix - k)
            dic[prefix] = 1 + dic.get(prefix, 0)
        return count
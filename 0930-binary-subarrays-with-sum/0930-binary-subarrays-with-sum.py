class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = count = 0
        dic = dict()
        for val in nums:
            prefix += val
            if prefix == goal:
                count += 1
            if dic.get(prefix - goal):
                count += dic.get(prefix - goal)
            dic[prefix] = 1 + dic.get(prefix, 0)
        return count
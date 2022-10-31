class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic, count = dict(), 0
        for i in nums:
            if dic.get(i):
                count += dic.get(i)
            dic[i] = 1 + dic.get(i, 0)
        return count
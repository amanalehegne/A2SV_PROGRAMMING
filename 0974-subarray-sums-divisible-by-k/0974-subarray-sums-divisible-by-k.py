class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = count = 0
        dic = dict()
        for val in nums:
            prefix += val
            if not prefix % k:
                count += 1
            if dic.get(prefix % k):
                count += dic.get(prefix % k)
            dic[prefix % k] = 1 + dic.get(prefix % k, 0)
        return count
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = count = 0
        dic = dict()
        for i in nums:
            if i % 2:
                prefix += 1
            if prefix == k :
                count += 1
            if dic.get(prefix - k):
                count += dic.get(prefix - k)

            if dic.get(prefix):
                dic[prefix] += 1
            else:
                dic[prefix] = 1
        return count
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = sub_array = 0
        dic = {}
        for i, val in enumerate(nums):
            if val % 2 != 0:
                count += 1
            if count == k:
                sub_array += 1
            if dic.get(count - k):
                sub_array += dic.get(count - k)
            if dic.get(count):
                dic[count] += 1
            else:
                dic[count] = 1
        return sub_array
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = count = 0
        dic = dict()
        for i in nums:
            prefix += i
            if prefix == k:
                count += 1
            # For every prefix, there could be elements (subarray), that when removed makes it valid,
            # and since there are -ve values, our prefix is not monotonically increasing and thus could have multiple of those points
            # Then our count wouldn't ony increase by one, but by number of these points
            if dic.get(prefix - k):
                count += dic.get(prefix - k)

            # Putting the value in the list
            # Since we're adding elements as we go, when we check the dictionary, we only found points up to the current position
            if dic.get(prefix):
                dic[prefix] += 1
            else:
                dic[prefix] = 1
        return count
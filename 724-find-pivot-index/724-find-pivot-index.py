class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        # Create the prefix sum array
        for i in nums:
            prefix.append(prefix[-1] + i)
        i = 0
        while i < len(prefix) - 1:
            if prefix[i] == prefix[-1] - prefix[i + 1]:
                return i
            i += 1
        return -1
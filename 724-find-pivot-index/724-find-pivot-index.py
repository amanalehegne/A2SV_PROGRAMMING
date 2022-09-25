class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, ans = [], 0
        for i in nums:
            ans += i
            prefix.append(ans)
        for i, val in enumerate(nums):
            prev = prefix[i] - val
            next_ = prefix[len(prefix) - 1] - prefix[i]
            if prev == next_:
                return i
        return -1
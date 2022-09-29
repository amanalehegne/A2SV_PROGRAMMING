class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        odd = []
        count = 0
        while r < len(nums):
            if nums[r] % 2 != 0:
                odd.append(r)
            while len(odd) > k:
                if nums[l] % 2 != 0:
                    odd.pop(0)
                l += 1
            if len(odd) == k:
                count += odd[0] - l + 1
            r += 1
        return count

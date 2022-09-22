class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        maximum = 0
        flip = k
        ans = ""
        while r < len(nums):
            ans += str(nums[r])
            if nums[r] == 0 and flip == 0:
                while flip == 0:
                    if nums[l] == 0:
                        flip += 1
                    l += 1
                    ans = ans[1:]
            if flip > 0 and nums[r] == 0:
                flip -= 1
            maximum = max(maximum, r - l + 1)
            # print(f"{ans} - indexes: {str(l)} and {str(r)} => {str(r - l + 1)}")
            r += 1
        return maximum
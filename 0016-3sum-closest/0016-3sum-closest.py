class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = None
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1
                else:
                    sum3 = nums[i] + nums[l] + nums[r]
                    if sum3 == target:
                        return sum3
                    else:
                        if (not closest) or (abs(target - sum3) < abs(target - closest)):
                            closest = sum3
                        if sum3 > target:
                            r -= 1
                        else:
                            l += 1
        return closest
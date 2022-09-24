class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            if height[l] > height[r]:
                minimum_height = height[r]
                r -= 1
            else:
                minimum_height = height[l]
                l += 1
            area = minimum_height * width
            maximum = max(maximum, area)
        return maximum
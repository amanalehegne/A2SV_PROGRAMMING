class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            if height[l] > height[r]:
                base = height[r]
                r -= 1
            else:
                base = height[l]
                l += 1
            area = max(area, base * (r - l + 1))
        return area
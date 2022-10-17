class Solution:
    def maxArea(self, height: List[int]) -> int:
        # To maximize area, we start with the maximum width
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            width = r - l
            # Height is our limiting factor
            if height[l] > height[r]:
                tall = height[r]
                r -= 1
            else:
                tall = height[l]
                l += 1
            max_area = max(max_area, tall * width)
        return max_area
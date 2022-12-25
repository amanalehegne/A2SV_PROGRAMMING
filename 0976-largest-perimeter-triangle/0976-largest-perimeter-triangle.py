class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # we sort them because we need to maximize the paprameter
        # s1, s2, s3 => s3 < s1 + s2, s2 < s3 + s2, s2 < s3 + s4
        # Thus if our first window (size 3 becuase of triangle) isn't valid we remove the largest element.
        # This is because since it is the largest and if our triangle isn't valid we can be sure it's is the one causing the problem by bing greater than the sum of the other two sides
        nums.sort(reverse=True)
        length = len(nums)
        for i in range(length - 2):
            side1 = nums[i]
            side2 = nums[i + 1]
            side3 = nums[i + 2]
            if side1 < side2 + side3:
                return side1 + side2 + side3

        return 0
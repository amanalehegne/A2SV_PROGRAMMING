class Solution:
    def thirdMax(self, nums: List[int]) -> int:
            first = second = third = None
            for i in nums:
                if i == first or i == second or i == third:
                    continue
                if (not first) or i > first:
                    third = second
                    second = first
                    first = i
                elif (not second) or i > second:
                    third = second
                    second = i
                elif (not third) or i > third:
                    third = i
            if third is not None:
                return third
            return first
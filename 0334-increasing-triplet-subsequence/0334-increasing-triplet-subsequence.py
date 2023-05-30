class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        If we are concerned with bith the index and the values, we shouldn't sort them because:
        A) We have an ordering by default (that is their index)
        B) If we sort them we will get an a different form of ordering and lose the existing one (value and lose ordering of their index)
        """
        first = second = float('inf')
        size = len(nums)
        for i in range(size):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        
        return False
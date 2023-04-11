class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = float("inf")
        greatest = -float("inf")
        for i in nums:
            smallest = min(smallest, i)
            greatest = max(greatest, i)
        
        def GCD(num1, num2):
            if num2 == 0:
                return num1
            return GCD(num2, num1 % num2)
        
        return GCD(smallest, greatest)
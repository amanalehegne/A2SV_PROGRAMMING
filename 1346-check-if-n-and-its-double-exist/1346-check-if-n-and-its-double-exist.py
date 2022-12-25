class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # [-2,0,10,-19,4,6,-8]
        numbers = dict()
        for i, num in enumerate(arr):
            numbers[num] = i + 1
        
        for i, num in enumerate(arr):
            if numbers.get(num * 2) and numbers.get(num * 2) != i + 1:
                return True
        
        return False
        
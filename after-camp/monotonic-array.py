class Solution:
    def isMonotonic(self, arr: List[int]) -> bool:
        size = len(arr)
        increase = decrease = True
        for i in range(size - 1):
            if arr[i] > arr[i + 1]:
                decrease = False
            if arr[i] < arr[i + 1]:
                increase = False
        return decrease or increase

            



class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        length = len(arr)
        zero = 0
        for i in range(length):
            if not arr[zero] and arr[i]:
                arr[zero], arr[i] = arr[i], arr[zero]
            if arr[zero]:
                zero += 1
            if not arr[i]:
                continue
            
        
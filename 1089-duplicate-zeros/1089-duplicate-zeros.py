class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        index = 0
        for num in arr[:]:
            if num == 0:
                arr[index] = 0
                index += 1
                if index == len(arr):
                    break
                arr[index] = 0
            else:
                arr[index] = num
            index += 1
            if index == len(arr):
                break
        
        
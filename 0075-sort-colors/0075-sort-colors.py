class Solution:
    def sortColors(self, arr: List[int]) -> None:
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            if arr[j] > temp:
                while j >= 0 and arr[j] > temp:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = temp
        
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        index = 0
        length = len(arr)
        while index < length:
            if arr[index] == 0:
                for i in range(length - 1, index, -1):
                    arr[i] = arr[i - 1]
                arr[index] = 0
                index += 2
            else:
                index += 1


        
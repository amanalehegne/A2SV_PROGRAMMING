class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        length = len(arr)
        index = 0
        while index < length:
            num = arr[index]
            if not num:
                for i in range(length - index - 1):
                    arr[length - 1 - i] = arr[length - 2 - i]
                if index + 1 < length:
                    arr[index] = 0
                index += 2
            else:
                index += 1

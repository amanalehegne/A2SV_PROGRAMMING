class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1
        length = len(arr)
        for i in range(length):
            idx = length - 1 - i
            val = arr[idx]
            arr[idx] = maxVal
            if maxVal < val:
                maxVal = val
        return arr
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        rise = fall = False
        i = count = 0
        while i < len(arr):
            start = i
            while i + 1 < len(arr) and arr[i] < arr[i + 1]:
                i += 1
                rise = True
            if rise:
                while i + 1 < len(arr) and arr[i] > arr[i + 1]:
                    i += 1
                    fall = True
            if rise and fall:
                count = max(count, i - start + 1)
            else:
                i += 1
            rise = fall = False
        return count
        
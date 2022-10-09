class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        rise = fall = False
        mountain_size = i = 0
        while i < len(arr):
            l = i
            while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                i += 1
                rise = True
            # There must be rising before falling, else that wont be a mountain, it would be a valley
            if rise:
                while i < len(arr) - 1 and arr[i] > arr[i + 1]:
                    i += 1
                    fall = True
            if rise and fall:
                mountain_size = max(mountain_size, i - l + 1)
            # If we have no mountain starting at index i, we check the next index. In other cases however, we began from the end of the mountain. 
            # In this case however we have no mountain and check the next index point (i += 1)
            else:
                i += 1
            rise = fall = False
        return mountain_size
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        rising, falling = False, False
        i, mountain = 0, 0
        while i < len(arr) - 1:
            if arr[i] < arr[i + 1]:
                temp = i
                while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                    rising = True
                    i += 1
                while i < len(arr) - 1 and arr[i] > arr[i + 1]:
                    falling = True
                    i += 1
                if rising and falling:
                    mountain = max(mountain, i - temp + 1)
                    rising, falling = False, False
            else:
                i += 1
        return mountain
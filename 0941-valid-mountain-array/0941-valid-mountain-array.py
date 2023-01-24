class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = True
        down = False
        upCount = downCount = 0
        length = len(arr)
        for idx in range(length - 1):
            if up:
                if arr[idx] < arr[idx + 1]:
                    upCount += 1
                else:
                    up = False
                    down = True
            if down:
                if arr[idx] > arr[idx + 1]:
                    downCount += 1
                else:
                    break
        if upCount and downCount and upCount + downCount == length - 1:
            return True
        return False
        
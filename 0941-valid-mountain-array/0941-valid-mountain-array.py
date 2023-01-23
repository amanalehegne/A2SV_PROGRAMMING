class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = down = False
        length = len(arr)
        if length <= 1:
            return False
        # Move Up
        for idx in range(length - 1):
            if arr[idx] < arr[idx + 1]:
                up = True
            else:
                break
        i = idx
        # Move Down
        for idx in range(i, length - 1):
            if arr[idx] > arr[idx + 1]:
                down = True
            else:
                return False
        if up and down:
            return True
        return False
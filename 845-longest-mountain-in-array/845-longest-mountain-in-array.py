class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        peek, valley = False, False
        i = 0
        ans = 0
        while i < len(arr) - 1:
            if arr[i] < arr[i + 1]:
                temp = i
                while i < len(arr) -1 and arr[i] < arr[i + 1]:
                    i += 1
                    peek = True
                while i < len(arr) -1 and arr[i] > arr[i + 1]:
                    i += 1
                    valley = True
                if peek and valley:
                    ans = max(ans, i - temp + 1)
                peek, valley = False, False
            else:
                i += 1
        return ans
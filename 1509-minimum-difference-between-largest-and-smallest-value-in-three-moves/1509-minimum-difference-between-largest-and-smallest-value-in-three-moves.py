class Solution:
    def minDifference(self, arr: List[int]) -> int:
        """
        Options
        1) Remove All Elements from (the front and then the end)
        2) Remove The First 2 Elements from (the front and then the end) and the rest (1) from the reverse
        """
        if len(arr) <= 4:
            return 0
        
        arr.sort()
        print(arr)
        options = [
            arr[-1] - arr[3],
            arr[-4] - arr[0],
            arr[-2] - arr[2],
            arr[-3] - arr[1]
        ]
        return min(options)
        
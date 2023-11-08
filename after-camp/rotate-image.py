class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        rows = len(arr)
        for idx in range(rows):
            for i in range(idx, rows):
                arr[idx][i], arr[i][idx] = arr[i][idx], arr[idx][i]
        
        for lst in arr:
            lst.reverse()
        
        
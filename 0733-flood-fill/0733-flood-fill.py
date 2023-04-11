class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def check(row, col):
            cols = 0 <= col < len(image[0])
            rows = 0 <= row < len(image)
            return cols and rows
        
        val = [image[sr][sc]]
        seen = set()
        
        def DFS(row, col):
            if (not check(row, col)) or ((row, col) in seen) or image[row][col] != val[0]:
                return
            seen.add((row, col))
            image[row][col] = color
            
            DFS(row, col + 1)
            DFS(row, col - 1)
            DFS(row + 1, col)
            DFS(row - 1, col)
        
        DFS(sr, sc)
        return image
        
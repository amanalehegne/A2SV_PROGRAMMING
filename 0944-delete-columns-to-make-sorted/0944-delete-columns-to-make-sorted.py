class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)
        count = 0
        
        for col in range(cols):
            prev = None
            for row in range(rows):
                char = strs[row][col]
                if prev and char < prev:
                    count += 1
                    break;
                prev = char
        
        return count
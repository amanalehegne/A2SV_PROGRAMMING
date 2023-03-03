class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex - 1)
        length = len(prevRow)
        currentRow = [1] * (length + 1)
        for i in range(length - 1):
            currentRow[i + 1] = prevRow[i + 1] + prevRow[i]
        return currentRow
        
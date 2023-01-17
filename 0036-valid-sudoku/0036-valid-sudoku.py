class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Across and Top
        for row in range(9):
            dic = set()
            dic2 = set()
            for col in range(9):
                if (board[row][col].isdigit() and board[row][col] in dic) or (board[col][row].isdigit() and board[col][row] in dic2):
                    return False
                dic.add(board[row][col])
                dic2.add(board[col][row])

        colStart, colEnd = 0, 2
        rowStart, rowEnd = 0, 2
        index = 0
        # 3 X 3 'sub' martix
        for i in range(9):
            dic = set()
            for row in range(rowStart, rowEnd + 1):
                for col in range(colStart, colEnd + 1):
                    if board[row][col].isdigit() and board[row][col] in dic:
                        return False
                    dic.add(board[row][col])
            index += 1
            if index % 3 == 0:
                colStart, colEnd = 0, 2
                rowStart, rowEnd = rowStart + 3, rowEnd + 3
            else:
                colStart, colEnd = colStart + 3, colEnd + 3

        return True
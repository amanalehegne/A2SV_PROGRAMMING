class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        rows = len(matrix)
        cols = len(matrix[0])
        answerLength = 0
        up = True
        rowIndex = colIndex = 0


        while answerLength < (rows * cols):
            if up:
                # As we move upward our rows decreases and our column increases
                # For decreasing we have to check if it reaches zero
                # For increasing we check if it reaches the limit
                while rowIndex >= 0 and colIndex < cols:
                    answer.append(matrix[rowIndex][colIndex])
                    answerLength += 1
                    rowIndex -= 1
                    colIndex += 1

                # There is a possiblity we reach the corners
                # When this happens we're off in our column by one and row by two
                if colIndex == cols:
                    colIndex -= 1
                    rowIndex += 2
                else:
                    rowIndex += 1
            else:
                # As we move down, column indices are decreasing and row indices are increasing
                # Thus we have to check if column index reach zero and row index reach the limit
                while colIndex >= 0 and rowIndex < rows:
                    answer.append(matrix[rowIndex][colIndex])
                    answerLength += 1
                    colIndex -= 1
                    rowIndex += 1

                # There is a possiblity we hit the corners
                if rowIndex == rows:
                    rowIndex -= 1
                    colIndex += 2
                else:
                    colIndex += 1
            up = not up

        return answer
        
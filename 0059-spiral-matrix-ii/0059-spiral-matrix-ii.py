class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        length = n
        matrix = [[0] * length for i in range(length)]
        numbers = 0

        for index in range(length):
            lengthArray = len(matrix[index])

            # Across (Left To Right) (Top)
            for i in range(index, lengthArray - index):
                numbers += 1
                matrix[index][i] = numbers

            # Down (Right)
            for i in range(index + 1, lengthArray - index):
                numbers += 1
                temp = lengthArray - index - 1
                matrix[i][temp] = numbers

            # Across (Left To Right) (Bottom)
            for i in range(index + 1, lengthArray - index):
                numbers += 1
                matrix[length - 1 - index][lengthArray - 1 - i] = numbers

            # Up (Left)
            for i in range(index + 1, lengthArray - index - 1):
                numbers += 1
                matrix[lengthArray - 1 - i][index] = numbers

        return matrix
        
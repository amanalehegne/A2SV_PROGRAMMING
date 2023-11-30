class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Must have same slope
        # Slope m = (y2 - y1) / (x2 - x1)
        prev = None
        size = len(coordinates)
        for i in range(1, size):
            y = (coordinates[i][1] - coordinates[i - 1][1])
            x = (coordinates[i][0] - coordinates[i - 1][0])
            if x == 0:
                slope = -1
            else:
                slope = y / x
            if prev and prev != slope:
                return False
            prev = slope

        return True
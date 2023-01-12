class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens_set = {(x, y) for x, y in queens}
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        res = []

        for ix, iy in direction:
            x, y = king
            for i in range(7):
                x, y = x + ix, y + iy
                if (x, y) in queens_set:
                    res.append([x, y])
                    break
        return res
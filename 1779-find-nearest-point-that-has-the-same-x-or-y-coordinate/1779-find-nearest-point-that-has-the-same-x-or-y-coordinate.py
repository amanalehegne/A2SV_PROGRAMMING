class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = [math.inf, -1]
        for i, point in enumerate(points):
            xi, yi = point
            if xi == x or yi == y:
                distance = abs(x - xi) + abs(y - yi)
                if answer[0] > distance:
                    answer = [distance, i]
        
        return answer[-1]
        
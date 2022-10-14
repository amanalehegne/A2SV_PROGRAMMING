class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i, point in enumerate(points):
            x, y = point
            distance.append([(x * x) + (y * y), i])

        distance.sort(key=lambda x: x[0])
        ans = []
        for d, i in distance[:k]:
            ans.append(points[i])
        return ans
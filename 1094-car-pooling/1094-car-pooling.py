class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car_end = prefix = 0
        for num, start, end in trips:
            car_end = max(car_end, end)
        ans = [0] * (car_end + 1)
        for num, start, end in trips:
            ans[start] += num
            ans[end] += -num
        for i, val in enumerate(ans):
            prefix += val
            if prefix > capacity:
                return False
        return True
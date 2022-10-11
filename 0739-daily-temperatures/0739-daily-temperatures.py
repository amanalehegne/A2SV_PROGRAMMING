class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                index = stack.pop()
                wait[index] = (i - index)
            stack.append(i)
        return wait
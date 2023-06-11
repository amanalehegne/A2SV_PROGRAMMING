class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        one, two, three = 0, 1, 1
        for i in range(n - 2):
            current = one + two + three
            one, two, three = two, three, current
        return three

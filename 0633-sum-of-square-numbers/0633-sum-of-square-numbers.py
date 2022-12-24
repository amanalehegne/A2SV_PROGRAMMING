class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first = 0
        second = int(c ** 0.5)
        while first <= second:
            number = first**2 + second**2
            if number == c:
                return True
            elif number > c:
                second -= 1
            else:
                first += 1
        return False
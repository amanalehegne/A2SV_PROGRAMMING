class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [i for i in range(1, n+1)]
        index = 0
        for i in range(n - 1):
            index = (index + k - 1) % len(lst)
            lst.pop(index)
        return lst[0]
class Solution:
    def isHappy(self, n: int) -> bool:
        dic = dict()
        while n > 1:
            if dic.get(n):
                return False
            temp = 0
            for i in str(n):
                temp += (int(i) ** 2)
            dic[n] = True
            n = temp
        return True
                
class Solution:
    def intersect(self, num1: List[int], num2: List[int]) -> List[int]:
        dic = dict()
        ans = []
        if len(num1) < len(num2):
            for i in num1:
                if dic.get(i):
                    dic[i] += 1
                else:
                    dic[i] = 1
            for i in num2:
                if dic.get(i):
                    ans.append(i)
                    dic[i] -= 1
        else:
            for i in num2:
                if dic.get(i):
                    dic[i] += 1
                else:
                    dic[i] = 1
            for i in num1:
                if dic.get(i):
                    ans.append(i)
                    dic[i] -= 1
        return ans
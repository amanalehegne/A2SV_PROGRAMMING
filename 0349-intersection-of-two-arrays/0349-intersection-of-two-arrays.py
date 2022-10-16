class Solution:
    def intersection(self, num1: List[int], num2: List[int]) -> List[int]:
        dic = dict()
        ans = []
        if len(num1) < len(num2):
            for i in num1:
                dic[i] = True
            for i in num2:
                if dic.get(i):
                    ans.append(i)
                    dic[i] = False
        else:
            for i in num2:
                dic[i] = True
            for i in num1:
                if dic.get(i):
                    ans.append(i)
                    dic[i] = False
        return ans
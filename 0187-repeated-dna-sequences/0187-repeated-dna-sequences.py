class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return
        temp = []
        dic = dict()
        for r in range(10):
            temp.append(s[r])
        ans = dict()
        window = "".join(temp)
        for i in range(r + 1, len(s)):
            dic[window] = True
            temp.pop(0)
            temp.append(s[i])
            window = "".join(temp)
            if dic.get(window) and not ans.get(window):
                ans[window] = True
        if dic.get(window) and not ans.get(window):
            ans[window] = True
        temp = []
        for key in ans:
            temp.append(key)
        return temp
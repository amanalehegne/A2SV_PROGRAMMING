class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        dic = dict()
        for i in changed:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        ans = []
        for i in changed:
            if i == 0:
                if dic.get(i) >= 2:
                    dic[i] -= 2
                    ans.append(i)
            elif i > 0 and dic.get(i) and dic.get(i * 2):
                ans.append(i)
                dic[i * 2] -= 1
                dic[i] -= 1
        if len(ans) == len(changed) // 2:
            return ans
        return []
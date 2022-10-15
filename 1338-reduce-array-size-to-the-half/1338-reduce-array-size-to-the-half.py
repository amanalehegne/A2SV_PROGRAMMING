class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = dict()
        for i in arr:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1

        dic_lst = []
        for key in dic:
            dic_lst.append([key, dic.get(key)])
        dic_lst.sort(key=lambda x:x[1], reverse=True)

        count = reduced = 0
        for i, j in dic_lst:
            reduced += j
            count += 1
            if reduced >= len(arr) // 2:
                return count
        return count
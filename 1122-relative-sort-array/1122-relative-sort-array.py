class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = Counter(arr2)
        temp = []
        for num in arr1:
            if dic.get(num):
                dic[num] += 1
            else:
                temp.append(num)
        res = []
        for num in arr2:
            size = dic.get(num)
            for i in range(size - 1):
                res.append(num)
        temp.sort()
        for num in temp:
            res.append(num)

        return res
        
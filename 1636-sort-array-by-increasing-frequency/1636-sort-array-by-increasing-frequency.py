class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def compare(x, y):
            if x[1] > y[1]:
                return 1
            elif x[1] < y[1]:
                return -1
            else:
                if x[0] > y[0]:
                    return -1
                else:
                    return 1
                
        dic = Counter(nums)
        temp = []
        for key in dic:
            temp.append([key, dic.get(key)])
        
        temp.sort(key=cmp_to_key(compare))

        ans = []
        for x, y in temp:
            for i in range(y):
                ans.append(x)

        return ans
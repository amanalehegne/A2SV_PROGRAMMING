class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        temp = []
        for key in dic:
            temp.append([key, dic.get(key)])
        
        temp.sort(key= lambda x:(x[1], -x[0]))

        ans = []
        for x, y in temp:
            for i in range(y):
                ans.append(x)

        return ans
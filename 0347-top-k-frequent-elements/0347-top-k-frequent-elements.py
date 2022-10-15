class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for i in nums:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        arr = []
        for key in dic:
            arr.append([key, dic.get(key)])
        arr.sort(key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(arr[i][0])
        return ans
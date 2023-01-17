class Solution:
    def sortPeople(self, name: List[str], height: List[int]) -> List[str]:
        maxVal = max(height)
        temp = [0] * maxVal
        length = len(height)

        count = 0
        dic = dict()

        for i in range(length):
            if temp[height[i] - 1] == 0:
                count += 1
            temp[height[i] - 1] += 1
            dic[height[i] - 1] = name[i]

        ans = [0] * count
        index = count - 1
        for i in range(maxVal):
            size = temp[i]
            for j in range(size):
                ans[index] = dic.get(i)
                index -= 1

        return ans
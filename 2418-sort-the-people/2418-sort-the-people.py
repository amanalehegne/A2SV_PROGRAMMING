class Solution:
    def sortPeople(self, name: List[str], height: List[int]) -> List[str]:
        length = len(name)
        temp = []
        for i in range(length):
            temp.append([name[i], height[i]])
        temp.sort(key= lambda x:x[1], reverse=True)
        ans = []
        for x, y in temp:
            ans.append(x)
        return ans
        
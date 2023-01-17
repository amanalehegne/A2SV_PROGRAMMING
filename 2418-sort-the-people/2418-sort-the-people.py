class Solution:
    def sortPeople(self, name: List[str], height: List[int]) -> List[str]:
        length = len(name)

        for i in range(length):
            minIndex = i
            for j in range(i + 1, length):
                if height[minIndex] < height[j]:
                    minIndex = j
            if i != minIndex:
                height[minIndex], height[i] = height[i], height[minIndex]
                name[minIndex], name[i] = name[i], name[minIndex]
            

        return name
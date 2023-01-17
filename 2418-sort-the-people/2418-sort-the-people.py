class Solution:
    def sortPeople(self, name: List[str], height: List[int]) -> List[str]:
        length = len(name)
        for i in range(length):
            for j in range(length - i - 1):
                if height[j] < height[j + 1]:
                    height[j], height[j + 1] = height[j + 1], height[j]
                    name[j], name[j + 1] = name[j + 1], name[j]
    
        return name
class Solution:
    def sortPeople(self, name: List[str], height: List[int]) -> List[str]:
        length = len(height)
        for i in range(1, length):
            val = height[i]
            val2 = name[i]
            j = i - 1
            while j >= 0 and val > height[j]:
                height[j + 1] = height[j]
                name[j + 1] = name[j]
                j -= 1
            height[j + 1] = val
            name[j + 1] = val2
            
        return name
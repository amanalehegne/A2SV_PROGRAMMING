class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = dict()
        for i in range(len(position)):
            dic[position[i]] = (target - position[i]) / speed[i]
        position.sort()
        stack = []
        for i in range(1, len(position) + 1):
            if (not stack) or (stack[-1] < dic[position[-i]]):
                stack.append(dic[position[-i]])
        return len(stack)
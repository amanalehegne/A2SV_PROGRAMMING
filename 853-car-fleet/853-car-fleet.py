class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        for i in range(len(position)):
            dic[position[i]] = speed[i]
        position.sort()

        stack = []
        for index in range(1, len(position) + 1):
            rem = (target - position[-index]) / dic.get(position[-index])
            if stack and rem > stack[-1]:
                stack.append(rem)
            elif not stack:
                stack.append(rem)

        return len(stack)
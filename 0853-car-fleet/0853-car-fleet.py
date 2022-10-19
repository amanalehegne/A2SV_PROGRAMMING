class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = dict()
        for i in range(len(position)):
            dic[position[i]] = (target - position[i]) / speed[i]
        position.sort()
        prev = count = 0
        for i in range(1, len(position) + 1):
            if prev < dic[position[-i]]:
                prev = dic[position[-i]]
                count += 1
        return count
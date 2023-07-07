class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen = defaultdict(int)
        total = 0
        for num in answers:
            if seen[num] == 0 or seen[num] >= num + 1:
                total += (num + 1)
                seen[num] = 1
            else:
                seen[num] += 1

        return total
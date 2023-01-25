class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        right = len(skill) - 1
        left = res = 0
        prev = None
        while left < right:
            totalSkill = skill[left] + skill[right]
            if prev and prev != totalSkill:
                return -1
            res += (skill[left] * skill[right])
            left, right = left + 1, right - 1
            prev = totalSkill
        return res
        
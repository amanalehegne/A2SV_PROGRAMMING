class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0] * 2
        for bill in bills:
            if bill == 5:
                changes[0] += 5
            elif bill == 10:
                if changes[0] < 5:
                    return False
                changes[1] += 10
                changes[0] -= 5
            else:
                if changes[0] < 5:
                    return False
                if changes[1] > 0:
                    changes[1] -= 10
                    changes[0] -= 5
                elif changes[0] >= 15:
                    changes[0] -= 15
                else:
                    return False
        return True
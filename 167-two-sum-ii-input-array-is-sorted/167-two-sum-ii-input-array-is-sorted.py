class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while r < len(numbers):
            sum_val = numbers[l] + numbers[r]
            if sum_val == target:
                return [l + 1, r + 1]
            elif sum_val < target:
                l += 1
                r += 1
            else:
                while sum_val > target and l >= 0:
                    l -= 1
                    sum_val = numbers[l] + numbers[r]
                if sum_val == target:
                    return [l + 1, r + 1]
        return []
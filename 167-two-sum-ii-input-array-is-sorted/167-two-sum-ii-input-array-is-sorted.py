class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(numbers):
            if not dic.get(val):
                dic[target - val] = [val, i]
            else:
                return [dic.get(val)[1] + 1, i + 1]
        return []
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0
        foods = dict()
        for num in deliciousness:
            for i in range(22):
                if foods.get(2**i - num):
                    result += foods[2**i - num]
            foods[num] = 1 + foods.get(num, 0)
        return result % ((10 ** 9) + 7)



        
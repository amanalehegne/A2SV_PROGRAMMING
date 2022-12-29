class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # This question has the same approch as the [560. Subarray Sum Equals K]
        # We check for a pair in the dictionary and add values to the dictionary as we go
        result = 0
        foods = dict()
        for num in deliciousness:
            # Check if there exist a number that when added to our current number gave us
            # an answer that is a the root of 2 (2^N)
            for i in range(22):
                # If the that number exists, get its counts because they each yield a avalid pairs
                # e.g num = 1, 1, 1 => we could have (num[0], num[1]), (num[0], num[2]), (num[1], num[2])
                # Our pair count is equals to the number of count
                if foods.get(2**i - num):
                    result += foods[2**i - num]
            # For every number we get its count as we go
            foods[num] = 1 + foods.get(num, 0)
        # We get our answer [result] but the question asks as to return it as the mode of ((10 ^ 9) + 7)
        return result % ((10 ** 9) + 7)
        



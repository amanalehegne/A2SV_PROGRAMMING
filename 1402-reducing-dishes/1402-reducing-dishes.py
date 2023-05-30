class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        Case: [-1, -2, 0, 5, -9] => [5, 0, -1, -2, -9]
        Case: [-1, -8, 0, 5, -9] => [5, 0, -1, -8, -9]
        
        [5, 0, -1, -2, -9] => Lets hold the sum of the current Elements Value, and value of the previous premutation
        Formula = (prev + current) + size
        
        [5] => 5, current = ([5] = 5), prev = 5
        [5, 0] => (5 + 5) + -1 = 10, current = ([5, 0] = 5), prev = 10
        [5, 0, -1] => (10 + 5) + -1 = 14, current = ([5, 0, -1] => 4), prev = 14
        [5, 0, -1, -2] => (14 + 4) - 2
        
        
        """
        satisfaction.sort(reverse=True)
        print(satisfaction)
        
        size = len(satisfaction)
        res = 0
        elements = like_time = 0
        for i in range(size):
            like_time = elements + like_time + satisfaction[i]
            res = max(res, like_time)
            elements += satisfaction[i]
            
            
        return res
        
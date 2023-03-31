class Solution:
    def findComplement(self, num: int) -> int:
        base = 1
        # Get the number to the next greater power of two
        # For 5, that would be 8 => 1000
        # If we subtract one from the value we get, 8 - 1 = 7, 111
        # We ould get a binary representation that is equal to the length of the num, and also with all 1
        # From this we can get the complement by simply subtacting num from it
        # 111 - 101 => 010 | 7 - 5 = 2
        while num >= base:
            base <<= 1
        
        base -= 1
        
        return base - num
        
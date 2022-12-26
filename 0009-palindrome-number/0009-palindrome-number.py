class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        tempNum = num
        countDigit = 1
        while tempNum // 10:
            countDigit *= 10
            tempNum //= 10

        while num:
            numLeft = (num // countDigit) % 10
            rightNum = num % 10
            if numLeft != rightNum:
                return False
            num %= countDigit
            countDigit //= 100
            num //= 10
        return True
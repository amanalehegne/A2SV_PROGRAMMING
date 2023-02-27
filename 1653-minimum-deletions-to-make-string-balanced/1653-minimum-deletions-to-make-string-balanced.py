class Solution:
    def minimumDeletions(self, s):
        res, b = 0, 0
        for i in s:
            if i == 'b':
                b += 1
            elif b:
                res += 1
                b -= 1
        return res
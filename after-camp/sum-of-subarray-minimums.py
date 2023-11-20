class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        length = len(arr)
        res = prevVal = 0
        
        for i in range(length):
            forCount = 1
            while stack and stack[-1][0] > arr[i]:
                prev = stack.pop()
                forCount += prev[1]
                prevVal -= (prev[0] * prev[1])
                
            stack.append([arr[i], forCount])
            prevVal += (arr[i] * forCount)
            res += prevVal
        
        return res % (10 ** 9 + 7)
                
        
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prevSign = -1
        length = len(arr)
        if length == 1:
            return 1
        left = i = res = 0
        
        for i in range(length - 1):
            if arr[i] > arr[i + 1]:
                curSign = 1
            elif arr[i] < arr[i + 1]:
                curSign = 2
            else:
                curSign = 3

            if curSign == 3 or (curSign == prevSign):
                print(arr[left:i + 1])
                res = max(res, i - left + 1)
                left = i
                if curSign == 3:
                    left += 1
            prevSign = curSign
                
        print(left, i)
        return max(res, i - left + 2)
            
            
        
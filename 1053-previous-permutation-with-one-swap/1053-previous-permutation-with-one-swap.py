class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
        Lets iterate until we find a larger element (somethign that break our decending order form the end)
        Then we find the larget element in that set
        Finally we swap
        """
        
        size = len(arr)
        check = False
        for i in range(size - 1):
            idx = size - 1 - i
            if arr[idx] < arr[idx - 1]:
                check = True
                break
        
        idx1, idx2 = idx - 1, idx
        for i in range(idx, size):
            if arr[i] < arr[idx1] and arr[i] > arr[idx2]:
                idx2 = i
                
        if check:
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
            
        
        return arr
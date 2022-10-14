#User function Template for python3

class Solution: 
    def select(self, arr, i):
        current = absolute = i
        while absolute < len(arr):
            if arr[current] > arr[absolute]:
                current = absolute
            absolute += 1
        return current
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min_index = self.select(arr, i)
            if min_index != i:
                temp = arr[min_index]
                arr[min_index] = arr[i]
                arr[i] = temp
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
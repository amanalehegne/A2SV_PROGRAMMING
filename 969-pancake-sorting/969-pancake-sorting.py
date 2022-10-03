class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            index = self.get_max(arr, len(arr) - i)[1] + 1
            if index != len(arr) - i:
                self.flip(arr, index)
                self.flip(arr, len(arr) - i)
                ans.append(index)
                ans.append(len(arr) - i)
        return ans
    
    
    def flip(self, arr, k):
        i, j = 0, k - 1
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        return arr


    def get_max(self, arr, k):
        maximum = [arr[0], 0]
        for i in range(k):
            if maximum[0] < arr[i]:
                maximum[0] = arr[i]
                maximum[1] = i
        return maximum
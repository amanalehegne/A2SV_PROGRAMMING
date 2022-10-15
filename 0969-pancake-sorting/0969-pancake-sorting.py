class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        ans = []
        for i in range(n + 1):
            flip_index = self.get_max(arr, n - i)
            if flip_index != n - i:
                if flip_index > 0:
                    self.flip(arr, flip_index)
                    ans.append(flip_index + 1)
                self.flip(arr, n - i)
                ans.append(n - i + 1)
        return ans
    
    
    def get_max(self, arr, i):
        max = 0
        for i in range(i + 1):
            if arr[max] < arr[i]:
                max = i
        return max
    
    
    def flip(self, arr, r):
        l = 0
        while l < r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1
        return arr
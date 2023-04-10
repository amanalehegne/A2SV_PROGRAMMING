class Solution:
    def SieveOfEratosthenes(self, num):
        arr = [i + 2 for i in range(num - 1)]
        size = int(num ** 0.5)
        for i in range(size + 1):
            if arr[i] != -1:
                start = arr[i] * arr[i]
                for j in range(start, num + 1, arr[i]):
                    arr[j - 2] = -1

        return arr
    
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        arr = self.SieveOfEratosthenes(n)
        arr.pop()
        count = 0
        for i in arr:
            if i != -1:
                count += 1
        
        return count
        
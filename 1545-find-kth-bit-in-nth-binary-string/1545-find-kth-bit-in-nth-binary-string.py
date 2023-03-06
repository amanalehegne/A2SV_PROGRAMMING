class Solution:
    def findKthBitRec(self, n):
        if n == 1:
            return "0"
        prev = self.findKthBitRec(n - 1)
        return prev + "1" + self.reverse(prev)

    def reverse(self, s):
        arr = []
        for char in s:
            if char == "0":
                arr.append("1")
            else:
                arr.append("0")
        arr.reverse()
        return "".join(arr)
    
    def findKthBit(self, n: int, k: int) -> str:
        arr = self.findKthBitRec(n)
        print(arr)
        return arr[k - 1]
        
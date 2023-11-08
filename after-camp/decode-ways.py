class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        size = len(s)
        arr = [0] * (size + 1)
        arr[0] = arr[1] = 1

        for i in range(1, size):
            if s[i] == '0':
                if s[i - 1] not in {'1', '2'}:
                    return 0
                arr[i + 1] = arr[i - 1]
            else:
                arr[i + 1] = arr[i]
                val = s[i - 1] + s[i]
                if '10' <= val <= '26':
                    arr[i + 1] += arr[i - 1]

        return arr[-1]

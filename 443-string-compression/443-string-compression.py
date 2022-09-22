class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = []
        i = 0
        while i < len(chars):
            count = 1
            compressed.append(chars[i])
            r = i + 1
            if r < len(chars) and chars[r] == chars[i]:
                while r < len(chars) and chars[r] == chars[i]:
                    count += 1
                    r += 1
                i = r
            else:
                i += 1

            if count > 1:
                for digit in str(count):
                    compressed.append(digit)
        chars[:] = compressed
        print(chars)
        return len(compressed)
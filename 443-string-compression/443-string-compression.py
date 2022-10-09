class Solution:
    def compress(self, chars: List[str]) -> int:
        i, ans = 0, []
        while i < len(chars):
            count = 1
            ans.append(chars[i])
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                i += 1
                count += 1
            i += 1
            if count > 1:
                for j in str(count):
                    ans.append(j)
        chars[:len(ans)] = ans
        return len(ans)
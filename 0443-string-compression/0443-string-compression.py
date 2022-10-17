class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("/")
        temp = []
        prev = chars[0]
        count = 1
        for val in chars[1:]:
            if val == prev:
                count += 1
            else:
                temp.append(prev)
                if count > 1:
                    for i in str(count):
                        temp.append(i)
                count = 1
            prev = val
        chars[:] = temp[:len(temp)]
        return len(temp)
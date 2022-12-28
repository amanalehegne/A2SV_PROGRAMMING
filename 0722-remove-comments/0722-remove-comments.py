class Solution:
    def removeComments(self, source):
        buffer = []
        answer = []
        comment = False
        for line in source:
            length = len(line)
            index = 0
            while index < length:
                current = line[index]
                nxt = ""
                if index + 1 < length:
                    nxt = line[index + 1]
                if comment:
                    if current == "*" and nxt == "/":
                        index += 1
                        comment = False
                else:
                    if current == "/" and nxt == "/":
                        break
                    elif current == "/" and nxt == "*":
                        index += 1
                        comment = True
                    else:
                        buffer.append(current)
                index += 1

            if buffer and (not comment):
                answer.append("".join(buffer))
                buffer = []
        return answer
class Solution:
    def addSpaces(self, s: str, space: List[int]) -> str:
        lengthStr = len(s)
        spaceCount = len(space)
        ans = []

        count = 0
        spaceIndex = 0
        charIndex = 0
        spaceTimes = 0

        for i in range(lengthStr + spaceCount):
            if spaceIndex < spaceCount and count - spaceTimes == space[spaceIndex]:
                ans.append(" ")
                spaceIndex += 1
                spaceTimes += 1
            else:
                ans.append(s[charIndex])
                charIndex += 1
            count += 1

        return "".join(ans)
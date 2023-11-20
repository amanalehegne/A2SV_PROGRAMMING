class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        left = 0
        dna = set()
        res = set()
        for i in range(length):
            if i >= 9:
                sequence = s[left:i + 1]
                if sequence in dna:
                    res.add(sequence)
                dna.add(sequence)
                left += 1

        return list(res)
        
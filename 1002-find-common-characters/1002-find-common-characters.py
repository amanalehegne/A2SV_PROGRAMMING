class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        dic = Counter(words[0])
        for word in words:
            temp = Counter(word)

            for char in dic:
                dic[char] = min(dic[char], temp.get(char, 0))
                
        for key in dic:
            size = dic.get(key)
            for i in range(size):
                res.append(key)
                
        return res

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])
        for word in words:
            temp = Counter(word)
            for key in dic:
                dic[key] = min(dic.get(key), temp.get(key, 0))
        
        res = []
        for key in dic:
            if dic.get(key):
                factor = dic.get(key)
                for i in range(factor):
                    res.append(key)
        
        return res
        
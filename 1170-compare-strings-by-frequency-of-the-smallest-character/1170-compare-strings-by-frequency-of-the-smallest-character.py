class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def getSmallest(word):
            res = word[0]
            for char in word:
                res = min(res, char)
            
            return res
        
        def helper(words):
            res = []
            for word in words:
                count = Counter(word)
                char = getSmallest(list(count.keys()))
                res.append(count[char])
            
            return res
        
        def rightBisect(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                midPoint = left + (right - left) // 2
                
                if arr[midPoint] < target:
                    left = midPoint + 1
                else:
                    right = midPoint - 1
            
            return len(arr) - left
        
        queries = helper(queries)
        words = helper(words)
        words.sort()
        
        res = []
        for query in queries:
            val = rightBisect(words, query + 1)
            res.append(val)
        
        return res
        
            
        
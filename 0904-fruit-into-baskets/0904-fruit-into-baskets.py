class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = count = basket = 0
        dic = dict()
        while r < len(fruits):
            if dic.get(fruits[r]) or basket < 2:
                if dic.get(fruits[r]):
                    dic[fruits[r]] += 1
                else:
                    dic[fruits[r]] = 1
                    basket += 1
                r += 1
            else:
                count = max(count, r - l)
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    basket -= 1
                l += 1
        return max(count, r - l)
                
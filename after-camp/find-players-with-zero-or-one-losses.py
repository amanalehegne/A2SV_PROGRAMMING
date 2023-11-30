class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for winner, looser in matches:
            dic[looser] += 1
            dic[winner] = dic[winner]
        
        winner = []
        oneLose = []
        for key in dic:
            if dic[key] == 0:
                winner.append(key)
            elif dic[key] == 1:
                oneLose.append(key)
        
        return [sorted(winner), sorted(oneLose)]


        
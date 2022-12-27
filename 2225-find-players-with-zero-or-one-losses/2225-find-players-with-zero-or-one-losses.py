class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = dict()
        for winner, loser in matches:
            losers[loser] = 1 + losers.get(loser, 0)

        loserAnswer = []
        for key in losers:
            if losers.get(key) == 1:
                loserAnswer.append(key)

        winnerAnswer = []
        for winner, loser in matches:
            if not losers.get(winner):
                winnerAnswer.append(winner)
        winnerAnswer = list(set(winnerAnswer))

        winnerAnswer.sort()
        loserAnswer.sort()

        return [winnerAnswer, loserAnswer]
        
            
        
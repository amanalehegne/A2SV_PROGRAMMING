class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        playersLength = len(players)
        trainersLength = len(trainers)
        pairCount = 0
        
        players.sort()
        trainers.sort()
        
        playersIndex = trainersIndex = 0
        while playersIndex < playersLength and trainersIndex < trainersLength:
            if players[playersIndex] <= trainers[trainersIndex]:
                pairCount += 1
                trainersIndex += 1
                playersIndex += 1
            else:
                trainersIndex += 1
        
        return pairCount
                
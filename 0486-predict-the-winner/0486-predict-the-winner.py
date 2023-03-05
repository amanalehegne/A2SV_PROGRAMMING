class Solution:
    def PredictTheWinnerRec(self, nums, left, right):
        if left > right: return 0
        
        leftOnly = self.PredictTheWinnerRec(nums, left + 2, right)
        leftRight = self.PredictTheWinnerRec(nums, left + 1, right - 1)
        
        moveLeft = nums[left] + min(leftOnly, leftRight)
        
        rightOnly = self.PredictTheWinnerRec(nums, left, right - 2)
        
        moveRight = nums[right] + min(rightOnly, leftRight)
        
        return max(moveLeft, moveRight)
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        totalScore = sum(nums)
        player1 = self.PredictTheWinnerRec(nums, 0, len(nums) - 1)
        player2 = totalScore - player1
        
        if player2 > player1:
            return False
        return True
        
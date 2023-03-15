class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right, turn):
            # If we are out of elements, nobody gets point
            if left > right:
                return 0
            # If its our turn, we want to maximize our points and mimize the point our oponent could get because we are concerend in the existance of a possiblity for player one to win, and the way to check that would to increase player ones score and much as possible and decrease players twos
            if turn:
                # In every turn we have 2 choices, either to get the left or the right element
                return max(nums[left] + helper(left + 1, right, not turn), nums[right] + helper(left, right - 1, not turn))
            else:
                return min(-nums[left] + helper(left + 1, right, not turn), -nums[right] + helper(left, right - 1, not turn))
        
        # What we are doing is that when player one get a point we add it and when player 2 gets a point we subtract it, and if the final answer is positive or zero it means we have a possiblity where player one wins, otherwise in all possiblity player two wins
        val = helper(0, len(nums) - 1, True)
        if val < 0:
            return False
        return True
                
        
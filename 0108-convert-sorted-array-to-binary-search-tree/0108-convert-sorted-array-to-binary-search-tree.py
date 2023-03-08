# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums, left, right):
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            
            prevLeft = helper(nums, left, mid - 1)
            prevRight = helper(nums, mid + 1, right)

            node = TreeNode(nums[mid], prevLeft, prevRight)
            
            return node
        
        return helper(nums, 0, len(nums) - 1)
            
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def getIndex(lst, key):
            arr = sorted(lst)
            left = 0
            right = len(arr) - 1
            while left <= right:
                midPoint = left + (right - left) // 2
                
                if arr[midPoint] > key:
                    right = midPoint - 1
                else:
                    left = midPoint + 1
            
            return right
        
        def helper(arr):
            if not arr:
                return None
            
            parent = arr[0]
            split = getIndex(arr, parent)
            
            left = helper(arr[1:split+1])
            right = helper(arr[split+1:])
            
            node = TreeNode(parent, left, right)
            
            return node
            
            
        return helper(preorder)
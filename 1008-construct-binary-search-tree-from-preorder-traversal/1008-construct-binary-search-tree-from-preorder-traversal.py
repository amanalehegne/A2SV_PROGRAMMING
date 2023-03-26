# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def binarySearch(arr, key):
            left = 0
            right = len(arr) - 1
            
            while left <= right:
                midPoint = left + (right - left) // 2
                
                if arr[midPoint] == key:
                    return midPoint
                if arr[midPoint] > key:
                    right = midPoint - 1
                else:
                    left = midPoint + 1
            
            return 0
        
            
        def helper(preorder, inorder):
            if not preorder:
                return None
            
            parent = preorder[0]
            partition = binarySearch(inorder, parent)
            
            left = helper(preorder[1:partition + 1], inorder[:partition])
            right = helper(preorder[partition + 1:], inorder[partition + 1:])
            
            node = TreeNode(parent, left, right)
            
            return node
        
        res = helper(preorder, sorted(preorder))
        return res
        
        
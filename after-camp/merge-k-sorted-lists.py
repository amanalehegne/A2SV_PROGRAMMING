# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        size = len(lists)
        for i in range(size):
            node = lists[i]
            while node:
                arr.append([node.val, node])
                node = node.next
        arr.sort(key= lambda x:x[0])
        
        root = ListNode()
        current = root
        for i in range(len(arr)):
            val = arr[i][0]
            current.next = ListNode(val)
            current = current.next
        
        return root.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        great, less = [], []
        while head:
            if head.val < x:
                less.append(head)
            else:
                great.append(head)
            head = head.next
        arr = less + great
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        if arr:
            arr[-1].next = None
            return arr[0]
        return None
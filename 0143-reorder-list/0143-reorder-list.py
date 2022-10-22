# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        while head:
            arr.append(head)
            head= head.next

        for i in range(len(arr) // 2):
            arr[i].next = arr[len(arr) - 1 - i]
            if len(arr) - 1 - i > i + 1:
                arr[len(arr) - 1 - i].next = arr[i + 1]

        arr[len(arr) // 2].next = None

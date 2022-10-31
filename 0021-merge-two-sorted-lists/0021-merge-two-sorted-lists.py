# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        arr = []
        while p1 and p2:
            if p1.val < p2.val:
                arr.append(p1)
                p1 = p1.next
            else:
                arr.append(p2)
                p2 = p2.next
        while p1:
            arr.append(p1)
            p1 = p1.next
        while p2:
            arr.append(p2)
            p2 = p2.next
        if not arr:
            return
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        arr[-1].next = None
        return arr[0]
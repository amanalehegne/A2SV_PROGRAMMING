# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        obj = ListNode()
        ans = obj

        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            ans.next = ListNode(val)
            ans = ans.next
        while list1 is not None:
            ans.next = ListNode(list1.val)
            list1 = list1.next
            ans = ans.next
        while list2 is not None:
            ans.next = ListNode(list2.val)
            list2 = list2.next
            ans = ans.next
        return obj.next
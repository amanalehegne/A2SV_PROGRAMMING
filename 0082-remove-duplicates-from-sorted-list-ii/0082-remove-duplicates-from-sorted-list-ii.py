# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # The 'prev' is used as an anchor - to hook the element to the next non repeating element
        # 'cur' along with 'cur.next' is used to find non repeating elements
        # This was we have 3 pointers - prev, cur, cur.next. if cur and cur.next are similar, they move until they become unique
        # once we find a unique element we attach it to our previous(prev) element
        prev, cur = dummy, head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next
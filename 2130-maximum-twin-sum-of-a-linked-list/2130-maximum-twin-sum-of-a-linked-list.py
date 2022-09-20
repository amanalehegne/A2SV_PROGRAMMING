# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp, lst = head, []
        while temp:
            lst.append(temp.val)
            temp = temp.next
        maximum = 0
        for i in range(len(lst)):
            sum = lst[i] + lst[len(lst) - 1 - i]
            maximum = max(maximum, sum)
        return maximum
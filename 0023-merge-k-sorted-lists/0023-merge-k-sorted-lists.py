# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        size = len(lists)
        for i in range(size):
            head = lists[i]
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        dummy = ListNode(-1)
        res = dummy
        while heap:
            node = ListNode(heapq.heappop(heap))
            dummy.next = node
            dummy = dummy.next
        
        return res.next
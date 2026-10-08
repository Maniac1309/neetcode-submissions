# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        heap = []
        counter = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        while heap:
            value, count, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
        return dummy.next

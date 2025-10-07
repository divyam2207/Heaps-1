"""
TC: O(N log N) {where N is the total number of nodes across all k lists. We perform N insertions and N extractions on a heap of size up to N.}
SC: O(N) {The space is required to store all N node values inside the min-heap.}

Approach:

This problem is solved by using a **Min-Heap (Priority Queue)** to collect and sort all node values. The solution works in two main phases:

1.  **Collection**: We iterate through all $k$ linked lists and traverse every single node. The value of every node encountered is pushed onto a global min-heap. This process effectively flattens all $k$ sorted lists into one unsorted collection within the heap structure.
2.  **Construction**: After all values are collected, we build the final merged linked list. We repeatedly extract the smallest element from the min-heap and use that value to create a new `ListNode`. This ensures that the new list is built in non-decreasing order.

This approach correctly merges all lists into a single sorted list, though it is slightly less optimal than solutions that manage only the head nodes in the heap.

The problem ran successfully on LeetCode.
"""
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        heap = []

        for li in lists:
            curr = li
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        if heap:
            head = ListNode(heapq.heappop(heap))
            curr_node = head

            while heap:
                nxt = None
                if heap:
                    nxt = ListNode(heapq.heappop(heap))

                curr_node.next = nxt
                curr_node = nxt

            return head
            
        return None

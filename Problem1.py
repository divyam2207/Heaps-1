"""
TC: O(N log K) {where N is the number of elements in `nums` and K is the target rank. We perform N heap operations, but the heap size is capped at K, making each operation O(log K).}
SC: O(K) {The space is determined by the maximum size of the heap, which is constrained to K elements.}

Approach:

This problem is optimally solved using a **Min-Heap (Priority Queue)** of size $K$. The goal is to find the $k^{th}$ largest element, which is equivalent to finding the smallest element among the $k$ largest elements.

1.  **Initialization**: We maintain a min-heap that stores the $K$ largest elements encountered so far.
2.  **Streaming**: We iterate through the input array `nums` element by element.
3.  **Heap Management**: For every element:
    * We push the element onto the heap.
    * If the size of the heap exceeds $K$, we remove the smallest element from the heap using `heappop`. Since this is a min-heap, `heappop` always removes the root (the minimum element).
4.  **Result**: By maintaining a heap of size $K$, the smallest element remaining in the heap after iterating through the entire array must be the $k^{th}$ largest element overall. We extract and return this final element.

This approach is highly efficient because the heap size is bounded by $K$, minimizing the logarithmic cost of each heap operation.

The problem ran successfully on LeetCode.
"""
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for each in nums:

            heapq.heappush(heap, each)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)

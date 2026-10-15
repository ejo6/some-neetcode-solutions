class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)

            if s1 > s2: heapq.heappush(heap, -(s1 - s2))
        
        if len(heap) == 1: return -heap[0]
        return 0
       
       
       
        # --- 3.14 --- Version
        # heapq.heapify_max(stones)

        # while len(stones) > 1:
        #     s1 = heapq.heappop_max(stones)
        #     s2 = heapq.heappop_max(stones)

        #     if s1 > s2: heapq.heappush_max(stones, s1 - s2)

        # if len(stones) == 1: return stones[0]
        # return 0

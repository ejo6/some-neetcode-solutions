class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        # Put the remainder of numbers in
        for num in nums[k:]:
            # If it's larger than the smallest number
            if num > heap[0]: heapq.heapreplace(heap, num)
        
        # This is now the kth largest elements
        return heap[0]

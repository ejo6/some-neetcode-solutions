class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        
        # So we don't have to handle nulls
        self.upper.append(100001)
        self.lower.append(-100001)


    def addNum(self, num: int) -> None:
        upperMin = self.upper[0]
        lowerMax = self.lower[0]

        if num <= upperMin:
            heapq.heappush_max(self.lower, num)

            if not (len(self.lower) <= len(self.upper)):
                heapq.heappush(self.upper, heapq.heappop_max(self.lower))

        elif num >= lowerMax:
            heapq.heappush(self.upper, num)

            if not (len(self.lower) >= len(self.upper)):
                heapq.heappush_max(self.lower, heapq.heappop(self.upper))
        
    
    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return (self.upper[0] + self.lower[0]) / 2
        return self.upper[0] if len(self.upper) > len(self.lower) else self.lower[0]


        # Min heap -> minum number of the second half of numbers
        # Max heap -> max number of the first half of numbers

        # When a number comes in:
        #   if its smaller than the min.pop (upper):
        #       if the heaps are balanced or the min heap (upper) is larger:
        #           put in in the max heap (lower)
        #       if the max heap (lower) is larger:
        #           put in the max heap (lower), then pop the max and put that in min (upper)
        #
        #   if its larger than the max.pop (lower):
        #       if the heaps are balanced or the max heap (lower) is larger:
        #           put in in the min heap (upper)
        #       if the heaps are NOT balanced:
        #           put in the min heap (upper), then pop the min and put that in max (lower)    
        #   
        #   (should not execute) else: put it in the smaller heap (defualt ot the min)
        #
        #
        # When a median is requested:
        #   if the size of the heaps are equal:
        #       return (min.pop + max.pop) / 2
        #   else:
        #       return the pop off of the larger heap

        # Time (addNum): O(log (n)), note that average can be very fast O(1)
        # Space O(n), where n is the number digits that have streamed in

        # 8 4 5 0 1 9 7 2 3 6
        # [0 1 2 3 4]  [5 6 7 8 9]
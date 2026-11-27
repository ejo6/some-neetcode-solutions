class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        total = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # There is overlap
            if start < prevEnd: 
                total += 1
                prevEnd = min(end, prevEnd)
            # Valid Case
            else: 
                prevEnd = end
        
        return total
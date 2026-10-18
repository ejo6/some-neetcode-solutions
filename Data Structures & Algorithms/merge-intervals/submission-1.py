class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort the input by intervals[i][0]
        # 2. Start at the first interval, incrament the index and go until interval[i][1] < interval[i + 1][0]

        # Assume we can modify the input
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])

        return result
        # [[1,3],[1,5],[6,7]]
        # s = 1, e = 8, ns = 6
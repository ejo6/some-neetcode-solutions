from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        res = []

        starts = sorted(a for a, b in flowers)
        ends = sorted(b for a, b in flowers)
        for time in people:
            res.append((bisect_right(starts, time) - bisect_left(ends, time)))
        return res


        


            
        






        



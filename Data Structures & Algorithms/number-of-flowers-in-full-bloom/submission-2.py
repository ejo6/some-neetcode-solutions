class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        res = []

        def bl(arr: list[int], t: int) -> int:
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = l + (h - l) // 2
                if arr[mid] >= t:
                    h = mid - 1
                else:
                    l = mid + 1
            return l      


        def br(arr: list[int], t: int) -> int:
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = l + (h - l) // 2
                if arr[mid] <= t:
                    l = mid + 1
                else:
                    h = mid - 1
            return l
        
        starts = sorted(a for a, b in flowers)
        ends = sorted(b for a, b in flowers)
        for time in people:
            res.append((br(starts, time) - bl(ends, time)))
        return res






        



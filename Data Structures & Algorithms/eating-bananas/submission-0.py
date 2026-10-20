class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = low + (high - low) // 2

            time = 0
            for pile in piles:
                time += -(-pile // mid)
            if time <= h:
                high = mid
            else:
                low = mid + 1
        return low
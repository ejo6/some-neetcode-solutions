class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Core idea was:
        # We want a fast way to figure if our current card + i exists, and how many our left
        #   -> Occurance dict for O(1) lookup on all of those
        # We want a fast way to figure out what the next remaining smallest card is:
        #   -> Min heap
        # To solve: keep taking the lowest card, check if we can make a group:
        #   -> if not: return False
        #   -> else: decrament the counts of all the cards used
        # -> if we never can't make a group, once our minHeap is empty, return True


        if len(hand) % groupSize != 0:
            return False

        # Count table
        count = defaultdict(int)

        for card in hand:
            count[card] += 1

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            curr_min = minHeap[0]

            for i in range(curr_min, curr_min + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True


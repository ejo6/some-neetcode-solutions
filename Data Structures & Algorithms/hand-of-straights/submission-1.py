class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
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


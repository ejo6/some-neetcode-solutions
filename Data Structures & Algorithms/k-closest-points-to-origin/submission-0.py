class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            distances.append([distance, x, y])

        heapq.heapify(distances)

        result = []
        for i in range(k):
            coordinates = heapq.heappop(distances)
            result.append([coordinates[1], coordinates[2]]), 

        return result

        # min heap of size k to track the k closest points
        # start with heapifying points[0:k], then continue to iterate through each point
        # push the distance onto the minheap each time, removing any 
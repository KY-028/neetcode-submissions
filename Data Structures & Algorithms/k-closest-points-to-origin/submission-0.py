class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points = [[math.sqrt(p[0] ** 2 + p[1] ** 2), p[0], p[1]] for p in points]

        heapq.heapify(points)
        res = []

        for _ in range(k):
            distance, x, y = heapq.heappop(points)
            res.append([x, y])

        return res
class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        

    def addNum(self, num: int) -> None:
        # if the number belong sin the large heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        # if no nums yet, first put in small
        else:
            heapq.heappush(self.small, -num)

        # if the difference is now more than 1
        if len(self.small) > len(self.large) + 1:
            # more elements in small:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # if the small has more elements, get the largest element from small
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        # if equal (even nums)
        return (-1 * self.small[0] + self.large[0]) / 2.0

        
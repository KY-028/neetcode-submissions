class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # keep only the k largest numbers, delete the rest
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
            # now minHeap[0] is the kth largest!

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # add one, remove one, [0] always kth largest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        

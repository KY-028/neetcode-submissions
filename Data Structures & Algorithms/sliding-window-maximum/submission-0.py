class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # find the maximum for the first window
        ans = []
        highest = float('-inf')
        l = 0

        heap = []

        for i in range(k-1):
            heapq.heappush_max(heap, (nums[i], i))

        for i in range(k-1, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            while heap[0][1] <= i - k:
                heapq.heappop_max(heap)
            ans.append(heap[0][0])
        
        return ans
        

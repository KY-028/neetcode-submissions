class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []
        freq = defaultdict(int)
        # O(n)
        for t in tasks:
            freq[t] += 1
        
        # O(n)
        for task, frequency in freq.items():
            heap.append((-frequency, task))
        
        # O(n)
        heapq.heapify(heap)

        time = 0
        q = deque()
        while heap or q:
            time += 1

            if not heap: # then there's only some elements in the deque
                time = q[0][1] # fast forward the time
            elif heap:
                count = 1 + heapq.heappop(heap)[0] # how many tasks of this kind left still
                if count: # if we still need to have this task later
                    q.append((count, time + n)) # when it's available again
                    # NOTE: time + n is the point where it becomes avaialble for the next time
            if q and time == q[0][1]:  # if any task becomes available, add it back to heap
                count, _ = q.popleft()
                heapq.heappush(heap, (count, ""))
        return time


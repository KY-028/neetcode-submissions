class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles) # upper bound for k
        left = 1
        
        def finish(k):
            count = 0
            for bans in piles:
                count += (bans // k + int(bans % k > 0))
                print(count, k, bans)
            if count <= h:
                return True
            return False

        while left <= right:
            mid = (left + right) // 2
            if finish(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


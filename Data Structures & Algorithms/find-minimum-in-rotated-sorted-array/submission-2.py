class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        starting = nums[0]

        # edge case: not rotated
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        
        while l <= r:
            mid = (l+r)//2
            # is this the min element?
            if nums[mid] < nums[mid+1] < nums[mid-1]:
                return nums[mid]
            # turning point right after
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]
            # turning point on the left?
            elif nums[mid] < starting:
                r = mid - 1
            # turning point not yet encountered
            else:
                l = mid + 1
        
        return l

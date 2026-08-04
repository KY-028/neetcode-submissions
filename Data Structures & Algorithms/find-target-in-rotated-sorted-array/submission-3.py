class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        starting = nums[0]

        # is the target on the left half or right half?
        if target < starting: # right half
            rightHalf = True
        else:
            rightHalf = False

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if not rightHalf:
                # if mid is not in the left half yet
                if nums[mid] < starting:
                    r = mid - 1
                # if mid is in left half and greater
                elif nums[mid] > starting and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # if mid is not in the right half yet
                if nums[mid] >= starting:
                    l = mid + 1
                # if mid is in right half and smaller
                elif nums[mid] < starting and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
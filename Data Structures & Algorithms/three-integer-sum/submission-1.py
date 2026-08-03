class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = []
        for i in range(len(nums)-2):
            # fix i as the leftmost element we haven't checked

            # if this value is already > 0, end early
            if nums[i] > 0:
                break
            
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum == 0:
                    sols.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates (only worry about left side)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threesum < 0:
                    l += 1
                else:
                    r -= 1
                
        
        return sols

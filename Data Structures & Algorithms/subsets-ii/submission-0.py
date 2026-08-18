class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # choose to add this number (even if repeated, guaranteed new number, exactly once)
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # choose to add no more of this number
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res
            
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, idx):
        if len(nums) == idx:
            self.res.append(nums[:])
        
        # now process through all
        for i in range(idx, len(nums)):
            # at this index, swap 2 elements
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]
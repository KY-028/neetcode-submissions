class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # you can see every call to this function eventually
            # creates a unique combination sent to this base case block
            if i >= len(nums): # if index out of bounds
                res.append(subset.copy())
                return

            # choose to add this number
            subset.append(nums[i])
            dfs(i + 1)
            # choose to not add this number
            subset.pop()
            dfs(i + 1)

        dfs(0) # start from index 0
        return res

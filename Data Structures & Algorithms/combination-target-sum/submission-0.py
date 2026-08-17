class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            # choose to add every number
            for j in range(i, len(nums)):
                if total + nums[j] > target: # if exceeds don't call
                    return
                cur.append(nums[j])
                dfs(j, cur , total + nums[j]) # try to add this number
                cur.pop()
        
        dfs(0, [], 0)
        return res
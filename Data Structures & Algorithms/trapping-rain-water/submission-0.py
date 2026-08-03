class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            # whichever side with a smaller max moves its pointer for water
            if leftMax < rightMax:
                l += 1 # can there be water with the next index?
                leftMax = max(leftMax, height[l])
                # amount of water = height of left bar (since rightMax is higher)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res

        
        # monotonic stack
        """
        stack = []
        res = 0

        for i in range(len(height)):
            # treat this index as left bar?
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    # height of water trapped
                    h = min(right, left) - mid
                    # because consecutive height -> 0
                    # we always add to res whenever 2 bar can trap water
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res
        """


        
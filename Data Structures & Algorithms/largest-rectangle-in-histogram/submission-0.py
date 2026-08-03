class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Idea: track a stack of heights
        largest = 0
        stack = []
        heights.append(0)
        for idx, h in enumerate(heights):
            # find the last time a height >= current height occurs
            start = idx
            while stack:
                # can form a valid rectangle
                if stack[-1][0] >= h:
                    val, start = stack.pop()
                    largest = max(largest, (idx - start) * val)
                else:
                    break
            stack.append((h, start))
        return largest
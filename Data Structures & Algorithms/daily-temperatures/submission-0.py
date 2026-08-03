class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            if idx == 0:
                stack.append((temp, idx))
                continue

            # if this temp is higher
            while stack and temp > stack[-1][0]:
                tmp, tmp_idx = stack.pop()
                result[tmp_idx] = idx - tmp_idx

            stack.append((temp, idx))

        return result
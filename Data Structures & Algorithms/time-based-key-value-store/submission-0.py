from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if len(self.data[key]) == 0 or self.data[key][0][1] > timestamp:
            return ""
        l, r = 0, len(self.data[key])-1
        while l <= r:
            mid = (l + r) // 2
            if self.data[key][mid][1] == timestamp:
                return self.data[key][mid][0]
            elif self.data[key][mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return self.data[key][r][0]
                

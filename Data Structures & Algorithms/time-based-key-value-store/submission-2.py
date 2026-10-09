from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key)   # .get avoids creating an empty entry
        if not values:
            return ""

        left, right = 0, len(values) - 1
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]  # valid candidate, look for a later one
                left = mid + 1
            else:
                right = mid - 1
        return result
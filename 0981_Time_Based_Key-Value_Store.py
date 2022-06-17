from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash_t = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_t[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_t.__contains__(key):
            return ""
        length = len(self.hash_t[key])
        l, r = 0, length-1

        while(l <= r):
            mid = (l+r)//2
            if self.hash_t[key][mid][0] <= timestamp and (mid == length-1 or self.hash_t[key][mid+1][0] > timestamp):
                return self.hash_t[key][mid][1]
            elif timestamp < self.hash_t[key][mid][0]:
                r = mid - 1
                continue
            else:
                l = mid + 1
                continue
        return ""

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1)
timeMap.get("foo", 3)
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4)
timeMap.get("foo", 5)
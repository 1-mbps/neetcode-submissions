class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.db.get(key):
            self.db[key] = [(value,timestamp)]
        else:
            self.db[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.db.get(key)
        if not lst:
            return ""
        # print(f"Looking for {key} at t={timestamp} - {lst}")
        l = 0
        r = len(lst)-1
        res = ""
        while l <= r:
            m = (l+r) // 2
            # print(lst[m])
            if lst[m][1] == timestamp:
                return lst[m][0]
            elif lst[m][1] < timestamp:
                res = lst[m][0]
                l = m+1
            else:
                r = m-1
        return res

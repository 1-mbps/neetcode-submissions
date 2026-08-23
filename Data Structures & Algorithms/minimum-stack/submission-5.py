# push: (in this order): 4 2 7 6 0 1 8

# stack:
# 4
# 4 2
# 4 2 7
# 4 2 7 6
# 4 2 7 6 0
# 4 2 7 6 0 1
# 4 2 7 6 0 1 8

# minstack:
# 4
# 4 2
# 4 2 0

class MinStack:

    def __init__(self):
        self.stack = []
        self.m = float('inf')
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1] if self.mins else val))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


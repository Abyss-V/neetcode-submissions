class MinStack:

    def __init__(self):
        self.stack = []
        self.m = [float("inf")]

    def push(self, val: int) -> None:
        self.m.append(min(self.m[-1],val))
        self.stack.append(val)

    def pop(self) -> None:
        self.m.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.m[-1] == float("inf"):
            return 0
        return self.m[-1]
class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mn:
            self.mn.append(min(self.mn[-1],val))
        else:
            self.mn.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.mn:
            return 0
        return self.mn[-1]

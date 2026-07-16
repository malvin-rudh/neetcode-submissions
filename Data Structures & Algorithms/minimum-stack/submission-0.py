class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = float('inf')

    def push(self, val: int) -> None:
        if val < self.curr_min:
            self.curr_min = val
        self.stack.append((val, self.curr_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.curr_min = self.stack[-1][1]
            else:
                self.curr_min = float('inf')
            

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.curr_min if self.stack else None

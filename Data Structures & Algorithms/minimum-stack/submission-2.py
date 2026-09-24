class MinStack:

    def __init__(self):
        # (linked?) list and hash map?
        # we can push by adding to the head
        # view the head or pop it
        # if we want the min we will have some additional procedures
        # if the min gets popped we need to adjust
        # we could keep a secondary in order structure?
        # insertions are too long
        
        # our stack can store both the current min and the current added
        # we store the previous min
        self.stack = []
        self.minimum = None


    def push(self, val: int) -> None:
        prev_min = self.minimum
        self.minimum = min(val, val if self.minimum == None else self.minimum)
        self.stack.append((val, prev_min))
        

    def pop(self) -> None:
        tup = self.stack.pop()
        val = tup[0]
        self.minimum = tup[1]
        return val
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.minimum
        

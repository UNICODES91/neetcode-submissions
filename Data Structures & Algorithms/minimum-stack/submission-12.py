class MinStack:

    def __init__(self):
        self.stack = []
        self.last_min = []
        self.min = 2**31

    def push(self, val: int) -> None:
        """
        Each new value is stored as value and last_min
        last_min is the min value of the stack right after this value was pushed in
        Cab be further simplified using a tuple of (val, last_min) in stack rather than 2 stacks
        """
        if len(self.stack) == 0:
            self.stack.append(val)
            self.last_min.append(None)
            self.min = val

        elif val < self.min:
            # current min becomes last min for this value
            self.stack.append(val)
            self.last_min.append(self.min)
            self.min = val
            
        else:
            self.stack.append(val)
            self.last_min.append(self.min)
        
        # print(self.stack, self.last_min, self.min)


    def pop(self) -> None:
        """
        Just remove the last appended element
        """
        v = self.stack.pop()
        if v == self.min:
            self.min = self.last_min.pop()
        else:
            self.last_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

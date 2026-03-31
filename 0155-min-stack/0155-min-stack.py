class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        
        # Push to min_stack if it's empty OR the new value is <= the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Only pop if the stack is not empty
        if self.main_stack:
            popped_value = self.main_stack.pop()
            
            # If the popped value is the current minimum, remove it from min_stack too
            if popped_value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
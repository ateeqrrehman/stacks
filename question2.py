# -------------------- question2.py --------------------

class Stack:                                
    """Simple Last-In-First-Out (LIFO) stack."""  # doc-string for class

    def __init__(self) -> None:               # constructor
        self._items: list = []                # internal list to hold data
        pass                                  # placeholder (does nothing)

    def push(self, item):                     # add item on top
        self._items.append(item)              # list append is O(1)
        pass                                  # required stub

    def pop(self):                            # remove top item
        if self.is_empty():                   # under-flow check
            raise IndexError("pop from empty stack")  # crash early if empty
        return self._items.pop()              # list pop returns & removes last
        pass                                  # unreachable but requested

    def peek(self):                           # look at top item only
        if self.is_empty():                   # can’t peek empty stack
            raise IndexError("peek from empty stack")
        return self._items[-1]                # last element in list
        pass

    def is_empty(self) -> bool:               # True if stack holds nothing
        return len(self._items) == 0
        pass

    def __len__(self) -> int:                 # len(stack) support
        return len(self._items)
        pass

    def __repr__(self) -> str:                # nice string for debugging
        return f"Stack({self._items})"
        pass

# evaluatePostfix
# -------------------------------------------------------

def evaluatePostfix(exp: str) -> int:
    """
    Evaluate a whitespace-separated postfix expression like
    '2 1 + 3 *' and return the integer result.
    Division uses int(a / b) so the answer truncates toward 0.
    """
    stack = Stack()                           # stack stores numbers

    # dictionary mapping operator symbol to a lambda that combines a and b
    ops = {
        '+': lambda a, b: a + b,              # addition
        '-': lambda a, b: a - b,              # subtraction
        '*': lambda a, b: a * b,              # multiplication
        '/': lambda a, b: int(a / b),         # division → truncate toward 0
    }

    for token in exp.split():                 # process expression left→right
        if token in ops:                      # token is an operator
            b = stack.pop()                   # right operand (pop first)
            a = stack.pop()                   # left  operand
            result = ops[token](a, b)         # compute a (op) b
            stack.push(result)                # push result for future ops
        else:                                 # token is a number
            stack.push(int(token))            # convert text to int then push
        pass                                  # loop placeholder

    return stack.pop()                        # final value on stack = answer
    pass                                       # end of function


# print outputs to run it directly
# -------------------------------------------------------
if __name__ == "__main__":
    tests = [
        "2 1 + 3 *",                          # expected 9
        "5 1 2 + 4 * + 3 -",                  # expected 14
        "-10 -2 /",                           # expected 5
    ]
    print("Postfix Evaluation:")
    for t in tests:                           # iterate over sample strings
        print(f"{t!r:26} ➜ {evaluatePostfix(t)}")  # show expression and result
    pass                                      # placeholder at end of file

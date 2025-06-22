# -------------------- question1.py --------------------

class Stack:                                # create a class Stack
    """Simple Last-In-First-Out (LIFO) stack.""" 

    def __init__(self) -> None:             
        self._items: list = []              # Python list holds the data
        pass                                

    # core stack operations
    def push(self, item):                   # put an item on top
        self._items.append(item)            # list.append = O(1)
        pass

    def pop(self):                          # remove the top item
        if self.is_empty():                 # can’t pop if nothing there
            raise IndexError("pop from empty stack")
        return self._items.pop()            # list.pop returns last element
        pass                                # after return = unreachable but allowed

    def peek(self):                         # look at top without removing
        if self.is_empty():                 # same empty check
            raise IndexError("peek from empty stack")
        return self._items[-1]              # [-1] is last element
        pass

    # helper methods
    def is_empty(self) -> bool:             # True if stack has no items
        return len(self._items) == 0
        pass

    def __len__(self) -> int:               # name it as len(stack)
        return len(self._items)
        pass

    def __repr__(self) -> str:              # text when we print(stack)
        return f"Stack({self._items})"
        pass

# Valid-Parentheses
# -------------------------------------------------------
def isValidParentheses(s: str) -> bool:
    """
    Returns True when every open bracket in 's' is closed
    by the right type and in the right order, else False.
    """  # (spec requirement)

    stack = Stack()                         # holds opening brackets
    match = {')': '(', ']': '[', '}': '{'}  # map close → open

    for ch in s:                            # look at each character
        if ch in "([{":                     # opening bracket?
            stack.push(ch)                  # save it for later
        elif ch in ")]}":                   # closing bracket?
            # invalid if nothing to match OR wrong type on top
            if stack.is_empty() or stack.pop() != match[ch]:
                return False

    return stack.is_empty()                 # valid only if nothing left
    pass                                    # final placeholder


#  runs ONLY when execute
# -------------------------------------------------------
if __name__ == "__main__":
    samples = ["()", "([)]", "(([]){})", ""]  # quick test strings
    print("Valid-Parentheses Demo:")
    for s in samples:                         # show each result
        print(f"{s!r:12} ➜ {isValidParentheses(s)}")
    pass                                      # end

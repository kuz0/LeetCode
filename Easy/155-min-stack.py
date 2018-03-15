class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_stack) is 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.isEmpty():
            if self.top() == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
        return None

    def top(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.min_stack[-1]

    def isEmpty(self):
        return len(self.stack) < 1


if __name__ == "__main__":
    minstack = MinStack()
    minstack.push(2)
    minstack.push(0)
    minstack.push(3)
    minstack.push(0)
    print(minstack.getMin())
    minstack.pop()
    print(minstack.getMin())
    minstack.pop()
    print(minstack.getMin())
    minstack.pop()
    print(minstack.getMin())

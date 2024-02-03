# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
 

# Follow-up: Can you implement the stack using only one queue?

# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 622.7K
# Submissions
# 988K
# Acceptance Rate
# 63.0%



from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        # Add the new element to queue1
        self.queue1.append(x)
        # Move all elements back to queue1 from queue2
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        # Pop the top element from queue1
        return self.queue1.popleft()

    def top(self) -> int:
        # Return the top element from queue1 without removing it
        return self.queue1[0]

    def empty(self) -> bool:
        # Check if queue1 is empty
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

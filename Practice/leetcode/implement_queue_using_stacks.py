# https://leetcode.com/problems/implement-queue-using-stacks


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        try:
            return self.queue.pop(0)
        except IndexError:
            return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        try:
            return self.queue[0]
        except IndexError:
            return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        try:
            return True if len(self.queue) == 0 else False
        except IndexError:
            return None


# Your MyQueue object will be instantiated and called as such:
# x = int(input('input:'))
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# print(param_2)
# param_3 = obj.peek()
# param_4 = obj.empty()

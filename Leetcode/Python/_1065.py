class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if self.end <= start:
            if self.right:
                return self.right.insert(start, end)
            self.right = Node(start, end)
            return True
        elif self.start >= end:
            if self.left:
                return self.left.insert(start, end)
            self.left = Node(start, end)
            return True
        else:
            return False


class MyCalendar(object):

    def __init__(self):
        self.node = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.node:
            self.node = Node(start, end)
            return True
        else:
            return self.node.insert(start, end)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

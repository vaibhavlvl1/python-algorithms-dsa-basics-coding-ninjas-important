from PACKAGES import linked_list_node


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def push(self, value):
        node = linked_list_node(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        self.count -= 1
        data = self.head.data
        self.head = self.head.next
        return data

    def top(self):
        if not self.is_empty():
            return self.head.data
        else:
            return "Empty Stack"

    def size(self):
        return self.count


# s = Stack()
#
# for i in range(1, 10):
#     s.push(i)
#     print(f" Pushed {i} element on top is ", s.top(), f" And the count is {s.size()}")
#
# for j in range(11):
#     x = s.pop()
#     print(f"element popped is ", x, f"And the count is {s.size()}")

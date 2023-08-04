from PACKAGES import linked_list_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def enqueue(self, value):
        node = linked_list_node(value)

        self.count += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return "Queue Empty"
        self.count -= 1
        data = self.head.data
        self.head = self.head.next

        return data

    def front(self):
        if not self.is_empty():
            return self.head.data
        return "Queue Empty"

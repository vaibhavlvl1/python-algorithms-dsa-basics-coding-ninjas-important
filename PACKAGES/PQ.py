class PQNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority

# MIN PQ


class MinPQ:
    def __init__(self):
        self.pq = []

    def heapify_up(self):

        child_index = self.size()-1
        while child_index > 0:
            parent_index = (child_index - 1) // 2
            if self.pq[parent_index].priority > self.pq[child_index].priority:
                self.pq[parent_index], self.pq[child_index] = self.pq[child_index], self.pq[parent_index]
                child_index = parent_index
            else:
                break

    def insert(self, ele, priority):
        node = PQNode(ele, priority)
        self.pq.append(node)
        self.heapify_up()

    def heapify_down(self):
        n = self.size()

        parent_index = 0

        while 2*parent_index+2 < n:
            lci = 2*parent_index+1
            rci = 2*parent_index+2

            if self.pq[lci].priority < self.pq[rci].priority:
                min_index = lci
            else:
                min_index = rci

            if self.pq[parent_index].priority > self.pq[min_index].priority:
                self.pq[parent_index], self.pq[min_index] = self.pq[min_index], self.pq[parent_index]
                parent_index = min_index
            else:
                break

    def remove_min(self):
        if self.is_empty():
            return "Empty"
        temp = self.pq[0]
        self.pq[0] = self.pq[self.size()-1]
        self.pq.pop()
        self.heapify_down()

        return temp.ele

    def size(self):
        return len(self.pq)

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.pq[0].ele


# MAX PQ

class MaxPQ:
    def __init__(self):
        self.pq = []

    def heapify_up(self):

        child_index = self.size()-1
        while child_index > 0:
            parent_index = (child_index - 1) // 2
            if self.pq[parent_index].priority < self.pq[child_index].priority:
                self.pq[parent_index], self.pq[child_index] = self.pq[child_index], self.pq[parent_index]
                child_index = parent_index
            else:
                break

    def insert(self, ele, priority):
        node = PQNode(ele, priority)
        self.pq.append(node)
        self.heapify_up()

    def heapify_down(self):
        n = self.size()

        parent_index = 0

        while 2*parent_index+2 < n:
            lci = 2*parent_index+1
            rci = 2*parent_index+2

            if self.pq[lci].priority < self.pq[rci].priority:
                max_index = rci
            else:
                max_index = lci

            if self.pq[parent_index].priority < self.pq[max_index].priority:
                self.pq[parent_index], self.pq[max_index] = self.pq[max_index], self.pq[parent_index]
                parent_index = max_index
            else:
                break

    def remove_max(self):
        if self.is_empty():
            return "Empty"
        temp = self.pq[0]
        self.pq[0] = self.pq[self.size()-1]
        self.pq.pop()
        self.heapify_down()

        return temp.ele

    def size(self):
        return len(self.pq)

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.pq[0].ele

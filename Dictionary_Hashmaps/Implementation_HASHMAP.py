class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.buckets_size = 10
        self.buckets = [None] * self.buckets_size
        self.count = 0

    def load_factor(self):
        return self.count/self.buckets_size

    def size(self):
        return self.count

    def get_index(self, hc):
        return abs(hc % self.buckets_size)

    def rehash(self):
        self.buckets_size = 2*self.buckets_size
        previous_buckets_copy = self.buckets
        self.buckets = [None] * self.buckets_size
        self.count = 0

        for head in previous_buckets_copy:
            while head is not None:
                self.insert(head.key, head.value)

                head = head.next

    def insert(self, key, value):
        hc = hash(key)
        index = self.get_index(hc)

        head = self.buckets[index]

        while head is not None:
            if key == head.key:
                head.value = value
                return
            head = head.next


        head = self.buckets[index]
        node = MapNode(key, value)
        node.next = head
        self.buckets[index] = node
        self.count += 1
        print(key, value, self.load_factor())

        if self.load_factor() >= 0.7:
            self.rehash()

    def remove(self, key):
        hc = hash(key)
        index = self.get_index(hc)

        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.count -= 1
                    self.buckets[index] = head.next
                    return
                else:
                    prev.next = head.next
                    self.count -= 1
                    return
            prev = head
            head = head.next
        # print("Key Not Found")
        return None

    def print_map(self):
        for head in self.buckets:
            while head is not None:
                print(head.key, head.value,end="  ")
                head = head.next
            print("")






# H = HashMap()
# H.insert("A", 1)
# H.insert("B", 2)
# H.insert("C", 3)
# H.insert("D", 4)
# H.insert("E", 5)
# H.insert("F", 6)
# H.insert("G", 7)
# H.insert("H", 8)
# H.insert("I", 9)
# H.insert("J", 10)
# H.insert("K", 11)
# H.insert("L", 12)
#
# print(H.size())
#
# for i in range(26):
#     H.remove(chr(64+i))
#     print(H.size())


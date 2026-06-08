# Node of a doubly linked list
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class LRUCache:

    h: Node
    t: Node
    length: int
    values: dict

    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.values = {}

    def get(self, key):
        currun_node = self.values[key]
        if (currun_node is self.h):
            head_next = self.h.next
            head_next.prev = None
            self.h.next = None

            
            
        return self.t.data if key in self.values else -1

    def put(self, key, value):
        if self.length == self.capacity:
            pass
        else:
            node = None
            if self.length == 0:
                node = Node(None, None, value)
                self.h = node
                self.t = node
            else:
                node = Node(None, self.t, value)
                self.t.next = node
                t = node

            self.length += 1
            self.values[key] = node
    
    def printList(self):
        n = self.h
        while(n):
            print(n.data)
            n = n.next



c = LRUCache(2)

c.put(1, "A")
c.put(2, "B")

c.printList()
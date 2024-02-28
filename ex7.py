#ENSF 338 Exercise 7
def reverse(self):
    current = self.head
    prev = None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    self.head = prev

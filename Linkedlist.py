class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_nth(self, data, n):
        if n < 1:
            print("Invalid position")
            return

        if n == 1:
            self.insert_beginning(data)
            return

        current = self.head
        position = 1

        while current is not None and position < n - 1:
            current = current.next
            position += 1

        if current is None:
            print("Invalid position")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_nth(self, n):
        if n < 1 or self.head is None:
            print("Invalid position")
            return

        if n == 1:
            self.delete_beginning()
            return

        current = self.head
        position = 1

        while current.next is not None and position < n - 1:
            current = current.next
            position += 1

        if current.next is None:
            print("Invalid position")
            return

        current.next = current.next.next

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_nth(self, data, n):
        if n < 1 or n > self.length() + 1:
            print("Invalid position")
            return

        if n == 1:
            self.insert_beginning(data)
            return

        if n == self.length() + 1:
            self.insert_end(data)
            return

        current = self.head
        position = 1

        while position < n:
            current = current.next
            position += 1

        new_node = DNode(data)
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_nth(self, n):
        if n < 1 or n > self.length():
            print("Invalid position")
            return

        if n == 1:
            self.delete_beginning()
            return

        if n == self.length():
            self.delete_end()
            return

        current = self.head
        position = 1

        while position < n:
            current = current.next
            position += 1

        current.prev.next = current.next
        current.next.prev = current.prev

    def reverse(self):
        current = self.head

        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def insert_nth(self, data, n):
        if n < 1 or n > self.length() + 1:
            print("Invalid position")
            return

        if n == 1:
            self.insert_beginning(data)
            return

        if n == self.length() + 1:
            self.insert_end(data)
            return

        current = self.head
        position = 1

        while position < n - 1:
            current = current.next
            position += 1

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next

        current.next = self.head
        self.tail = current

    def delete_nth(self, n):
        if n < 1 or n > self.length():
            print("Invalid position")
            return

        if n == 1:
            self.delete_beginning()
            return

        if n == self.length():
            self.delete_end()
            return

        current = self.head
        position = 1

        while position < n - 1:
            current = current.next
            position += 1

        current.next = current.next.next

    def reverse(self):
        if self.head is None or self.head == self.tail:
            return

        old_head = self.head
        previous = self.tail
        current = self.head

        while True:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

            if current == old_head:
                break

        self.head = previous
        self.tail = old_head
        self.tail.next = self.head

    def length(self):
        if self.head is None:
            return 0

        count = 1
        current = self.head.next

        while current != self.head:
            count += 1
            current = current.next

        return count

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")
sll = SLL()
sll.insert_end(10)
sll.insert_end(20)
sll.insert_beginning(5)
sll.insert_nth(15, 3)
sll.display()
print("Length:", sll.length())
sll.reverse()
sll.display()

print()

dll = DLL()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_beginning(5)
dll.insert_nth(15, 3)
dll.display()
print("Length:", dll.length())
dll.reverse()
dll.display()

print()

cll = CLL()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_beginning(5)
cll.insert_nth(15, 3)
cll.display()
print("Length:", cll.length())
cll.reverse()
cll.display()
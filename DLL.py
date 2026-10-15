
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # 3. Insert at nth position (1-based)
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

        if current == self.tail:
            self.insert_end(data)
            return

        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

    # 4. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # 5. Delete from end
    def delete_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # 6. Delete from nth position (1-based)
    def delete_nth(self, n):
        if n < 1 or self.head is None:
            print("Invalid position or empty list")
            return

        if n == 1:
            self.delete_beginning()
            return

        current = self.head
        position = 1

        while current is not None and position < n:
            current = current.next
            position += 1

        if current is None:
            print("Invalid position")
            return

        if current == self.tail:
            self.delete_end()
            return

        current.prev.next = current.next
        current.next.prev = current.prev

    # 7. Reverse the list
    def reverse(self):
        current = self.head

        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    # Display the list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


# Example usage
dll = DLL()

dll.insert_beginning(20)
dll.insert_beginning(10)
dll.insert_end(40)
dll.insert_nth(30, 3)

print("Original list:")
dll.display()

dll.delete_beginning()
dll.delete_end()
dll.delete_nth(2)

print("After deletions:")
dll.display()

dll.reverse()

print("After reversing:")
dll.display()

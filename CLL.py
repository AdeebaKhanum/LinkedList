
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    # 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
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

        while current is not self.tail and position < n - 1:
            current = current.next
            position += 1

        if position != n - 1:
            print("Invalid position")
            return

        if current == self.tail:
            self.insert_end(data)
            return

        new_node = Node(data)
        new_node.next = current.next
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
            self.tail.next = self.head

    # 5. Delete from end
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

        while current != self.tail and position < n - 1:
            current = current.next
            position += 1

        if current == self.tail or current.next == self.head:
            print("Invalid position")
            return

        target = current.next
        current.next = target.next

        if target == self.tail:
            self.tail = current
            self.tail.next = self.head

    # 7. Reverse the circular linked list
    def reverse(self):
        if self.head is None or self.head == self.tail:
            return

        old_head = self.head
        prev = self.tail
        current = self.head

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            if current == old_head:
                break

        self.head = prev
        self.tail = old_head
        self.tail.next = self.head

    # Display the list
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


# Example usage
cll = CLL()

cll.insert_beginning(20)
cll.insert_beginning(10)
cll.insert_end(40)
cll.insert_nth(30, 3)

print("Original list:")
cll.display()

cll.delete_beginning()
cll.delete_end()
cll.delete_nth(2)

print("After deletions:")
cll.display()

cll.reverse()

print("After reversing:")
cll.display()

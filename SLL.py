
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

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

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # 4. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 5. Delete from end
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

        while current.next is not None and position < n - 1:
            current = current.next
            position += 1

        if current.next is None:
            print("Invalid position")
            return

        current.next = current.next.next

    # 7. Reverse the list
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Display the list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example
sll = SLL()

sll.insert_beginning(20)
sll.insert_beginning(10)
sll.insert_end(40)
sll.insert_nth(30, 3)

sll.display()       # 10 -> 20 -> 30 -> 40 -> None

sll.delete_beginning()
sll.delete_end()
sll.delete_nth(2)

sll.display()       # 20 -> None

sll.reverse()
sll.display()       # 20 -> None

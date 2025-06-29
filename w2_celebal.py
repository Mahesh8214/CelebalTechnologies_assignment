# Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list.

# Defining a Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Defining the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Adding a node to the end
    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Print the list
    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Delete the nth node (1-based index)
    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise Exception("Index must be 1 or more.")

            # Delete first node
            if n == 1:
                deleted = self.head.data
                self.head = self.head.next
                print(f"Deleted node with value: {deleted}")
                return

            current = self.head
            for _ in range(n - 2):
                if current.next is None:
                    raise Exception("Index out of range.")
                current = current.next

            if current.next is None:
                raise Exception("Index out of range.")

            deleted = current.next.data
            current.next = current.next.next
            print(f"Deleted node with value: {deleted}")

        except Exception as e:
            print("Error:", e)


def main():
    ll = LinkedList()

    while True:
        print("\n--- Menu ---")
        print("1. Add node to end")
        print("2. Print list")
        print("3. Delete nth node")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            val = input("Enter value to add: ")
            ll.add_to_end(val)
            print(f"{val} added to the list.")

        elif choice == '2':
            print("Current List:")
            ll.print_list()

        elif choice == '3':
            try:
                pos = int(input("Enter position to delete: "))
                ll.delete_nth_node(pos)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()

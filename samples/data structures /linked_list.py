# PROBLEM: Build a simple linked list and print its values.
# INPUT: 4 then 10 20 30 40
# OUTPUT: 10 20 30 40

class Node:
    def __init__(self, value):
        self.value = value  # Data stored in this node.
        self.next = None    # Link to the next node.

n = int(input())
numbers = list(map(int, input().split()))
head = None
tail = None

for number in numbers:
    new_node = Node(number)

    if head is None:
        head = new_node  # First node becomes the head.
        tail = new_node
    else:
        tail.next = new_node  # Attach after the last node.
        tail = new_node

current = head
while current is not None:
    print(current.value, end=" ")
    current = current.next

print()

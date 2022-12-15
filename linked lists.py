"""

The calls will be in the form:

L = create_lists("task1.inp", 1)
match_ends(L)


L1, L2 = create_lists("task2.inp", 2)
L3 = reverse_and_concatenate(L1, L2)
L3.print_contents()

"""

class Node:
    def __init__(self, element, next):
        self.data = element
        self.next = next

class LinkedList:
    def __init__(self, taskNo):
        self.head = None  # Reference to head node
        self.size = 0  # Size of Linked List
        self.taskNo = taskNo  # Taskno, integer 1 or 2

    def insert_last(self, e):
        if self.head is None:
            self.head = Node(e, None)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(e, None)
        self.size += 1

    def print_contents(self):
        format_str = "%s" if self.taskNo == 1 else "%d"
        if self.size == 0:
            print(" ")
            return
        current = self.head
        while (current.next != None):
            print((format_str + " -> ") % current.data, end="")
            current = current.next

        print(format_str % current.data)


def create_lists(filename, taskNo):
    if taskNo == 1:
        L = LinkedList(taskNo)
        with open(filename) as f:
            for i in f.readline():
                L.insert_last(i)
        return L

    elif taskNo == 2:
        L1 = LinkedList(taskNo)
        L2 = LinkedList(taskNo)
        with open("task2.inp") as f:

            one = f.readline().strip().replace(" ", "")
            for i in one:
                i = int(i)
                L1.insert_last(i)

            two = f.readline().replace(" ", "")
            for i in two:
                i = int(i)
                L2.insert_last(i)

        return L1, L2


def reverse_and_concatenate(L1, L2):
    def reverse(L):
        current = L.head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        L.head = prev
        return L

    L3 = LinkedList(2)
    reverse(L1)
    reverse(L2)

    current1 = L1.head
    current2 = L2.head

    while current1 != None and current2 != None:
        L3.insert_last(current1.data)
        L3.insert_last(current2.data)
        current1 = current1.next
        current2 = current2.next

    if current1 != None:
        while current1 != None:
            L3.insert_last(current1.data)
            current1 = current1.next

    elif current2 != None:
        while current2 != None:
            L3.insert_last(current2.data)
            current2 = current2.next

    return L3


def match_ends(L):
    w = ""
    wR = ""
    i = 0
    current = L.head

    while current is not None:
        if i < L.size / 2:
            w = w + current.data
            current = current.next
            i += 1
        elif i >= L.size / 2:
            wR = wR + current.data
            current = current.next
            i += 1

    return w == wR[::-1]



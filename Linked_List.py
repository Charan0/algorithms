class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        if self.head == None:
            self.head = Node()
            self.head.data = new_data
        else:
            new_Node = Node()
            new_Node.data = new_data
            new_Node.next = None
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_Node

    def push(self, new_data):
        new_Node = Node()
        new_Node.data = new_data
        new_Node.next = self.head
        self.head = new_Node

    def insertAfter(self, pos, new_data):
        temp = self.head
        for _ in range(pos-1):
            temp = temp.next
        prev_Node = temp
        if prev_Node is None:
            print("The given previous Node is not in the linked list")
            return
        new_Node = Node()
        new_Node.data = new_data
        new_Node.next = prev_Node.next
        prev_Node.next = new_Node

    def append(self, new_data):
        new_Node = Node()
        new_Node.data = new_data
        if self.head is None:
            self.head = new_Node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_Node

    def deleteKey(self, key):
        
        temp = self.head
        if temp is not None:
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if (temp.data == key):
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next
        temp = None

    def deleteNode(self, pos):
        if self.head is None:
            return
        
        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                return
        
        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next

    def length(self):
        len = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            len += 1
        return len

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


llist = LinkedList()
print("Enter the elements you want to store in the list: ")
lstElements = list(map(int, input().split()))
for i in lstElements:
    llist.insert(i)
position = int(input("Enter the position after which you want to enter the number: "))
number = int(input("Enter the number which you want to enter: "))
llist.insertAfter(position, number)
llist.printList()

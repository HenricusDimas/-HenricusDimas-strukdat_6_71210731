class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_pos = None

    def addElementHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current_pos = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addElementTail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.current_pos = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def maju(self, step):
        node = self.current_pos
        for i in range(step):
            if node.next is not None:
                node = node.next
            else:
                node = self.head
        self.current_pos = node
        print(node.data)

    def mundur(self, step):
        node = self.current_pos
        for i in range(step):
            if node.prev is not None:
                node = node.prev
            else:
                node = self.tail
        self.current_pos = node
        print(node.data)

linkedlist = LinkedList()
linkedlist.addElementHead("Jogja")
linkedlist.addElementHead("Jakarta")
linkedlist.addElementTail("Bali")
linkedlist.addElementTail("Bandung")

linkedlist.maju(2) 
linkedlist.mundur(1) 
linkedlist.maju(5) 
linkedlist.mundur(3) 

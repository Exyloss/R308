#!/usr/bin/env python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def printNode(self):
        print(self.data, end=" ")
        if self.next != None:
            self.next.printNode()

    def printNodeRev(self):
        if self.next != None:
            self.next.printNodeRev()
        print(self.data, end=" ")

    def reverse(self, ll):
        ll.addInHead(self.data)
        if self.next != None:
            self.next.reverse(ll)
        return ll
    """
    def reverseList(self, l):
        tmp = Node(self.data)
        tmp.next = l
        if self.next is not None:
            tmp = self.next.reverseList(tmp)
        return tmp

    """

    def addInTail(self, value):
        if self.next == None:
            tmp = Node(value)
            self.next = tmp
        else:
            self.next.addInTail(value)

    def insert(self, value):
        if self.next != None and value > self.next.data:
            self.next.insert(value)
        else:
            tmp = Node(value)
            tmp.next = self.next
            self.next = tmp

class LinkedList:
    def __init__(self, head):
        self.head = head

    def printListRec(self):
        self.head.printNode()

    def printListRecRev(self):
        self.head.printNodeRev()

    def addInHead(self, value):
        i = self.head
        self.head = Node(value)
        self.head.next = i

    def addInTail(self, value):
        if self.head == None:
            self.addInHead(value)
        else:
            self.head.addInTail(value)

    def addSorted(self, value):
        if self.head == None or self.head.data > value:
            self.addInHead(value)
        else:
            self.head.insert(value)

    def reverse(self):
        ll = self.head.reverse(LinkedList(None))
        self.head = ll.head
        """
        temp = LinkedList()
        if self.head is not None:
            temp.head = self.head.reverseList(temp.head)
        return temp
        """




n1 = Node(0)
liste = LinkedList(n1)
n2 = Node(2)
n3 = Node(4)
n4 = Node(6)
n5 = Node(8)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

liste.addInHead(-2)
liste.addInTail(10)
liste.addSorted(7)
#liste.printListRecRev()
liste.reverse()
liste.printListRec()

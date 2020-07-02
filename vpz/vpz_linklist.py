class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def remove(self, key):
        temp = self.head
        if temp and temp.data == key:
        	self.head = temp.next
        	return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next

    def show(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
 
llist = LinkedList()
llist.add(7)
llist.add(1)
llist.add(3)
llist.add(2)
print("show")
llist.show()
llist.remove(1)
print("delete 1")
llist.show()
llist.remove(7)
print("delete 7")
llist.show()
llist.remove(4)
print("delete 4")
llist.show()
llist.remove(2)
print("delete 2")
llist.show()
"""
Modified linkedlist to include hash_value
"""


class Node:

    def __init__(self, key, initdata):
        self.key = key
        self.data = initdata
        self.next = None

    def getKey(self):
        return self.key

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, key, newdata):
        self.key = key
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, key, item):
        temp = Node(key, item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.getNext()

        return count

    def searchByKey(self, key):
        found = False
        current = self.head
        while current is not None and not found:
            if current.getKey() == key:
                return current
            current = current.getNext()

        return found

    def search(self, item):
        found = False
        current = self.head
        while current is not None and not found:
            if current.getData() == item:
                return current
            current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        if current.getData() == item:
            self.head = self.head.getNext()

        while current.getNext() is not None:
            next = current.getNext()
            if next.getData() == item:
                current.setNext(next.getNext())
                break
            else:
                current = current.getNext()

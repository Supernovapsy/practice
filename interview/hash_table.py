hashL = 5
def my_hash(obj):
    return hash(obj) % hashL

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.occupied = False

    def set(self, key, value):
        self.occupied = True
        n = self.head
        while n:
            # Overwrite if the key already is stored.
            if n.key == key:
                n.value = value
                return
            n = n.next
        node = Node(key, value)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node

    def get(self, key):
        if not self.occupied:
            raise Exception("Element does not exist")
        n = self.head
        while n:
            if n.key == key:
                return n.value
            n = n.next
        raise Exception("Element does not exist")

    def delete(self, key):
        if not self.occupied:
            raise Exception("Element does not exist")
        if self.head.key == key:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        n1 = self.head
        n2 = self.head.next
        while n2:
            if n2.key == key:
                n1.next = n2.next
                if self.tail == n2:
                    self.tail = n1
                    return
            n2 = n2.next
            n1 = n1.next
        raise Exception("Element does not exist")

class HashTable(object):
    def __init__(self):
        self.lst = list()
        for i in range(hashL):
            self.lst.append(HashList())

    def __getitem__(self, key):
        return self.lst[my_hash(key)].get(key)

    def __setitem__(self, key, value):
        self.lst[my_hash(key)].set(key, value)

    def __delitem__(self, key):
        self.lst[my_hash(key)].delete(key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
        except:
            return False
        return True

table = HashTable()
table["hello"] = "world"
print table["hello"]

for i in range(10):
    table[i] = i * i

del table[5]
del table[3]
del table[4]
del table[6]

for i in reversed(range(10)):
    if i in table:
        print table[i]

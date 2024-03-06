# hash table collison handling with separate chaining


class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            c = ord(char)
            hash += c

        return hash % self.max

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                break


ht = Hashtable()

ht['march 6'] = 325
ht['march 8'] = 345
ht['march 7'] = 330
ht['march 17'] = 335
print(ht.arr)
print(ht['march 6'])
ht['march 6'] = 355
print(ht.arr)
print(ht['march 6'])
del ht['march 8']
print(ht.arr)




            
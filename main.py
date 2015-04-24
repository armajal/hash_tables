# Implement hash tables in 3 different ways

# Use python dictionary
class OurDictionary():
    def __init__(self):
        self.dict = {}
    def add_key_value_pair(self, key, val):
        self.dict[key] = val
    def get_value(self, key):
        return self.dict[key]
    def remove_key(self, key):
        del self.dict[key]


# Use array
class OurDictionary2():
    def __init__(self):
        self.dict = []
    def add_key_value_pair(self, key, val):
        for i in self.dict:
            if i[0] == key:
                i[1] = val
                return
        self.dict.append([key,val])
    def get_value(self, key):
        for i in self.dict:
            if i[0] == key:
                return i[1]      
        raise KeyError
    def remove_key(self, key):
        for i in self.dict:
            if i[0] == key:
                self.dict.remove(i)


def get_fancy_index(ourlist, key):
    if (len(ourlist) == 0):
        return (0,False)

    start = 0
    end = len(ourlist) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        # Find the midpoint of the array
        if (ourlist[mid][0] == key):
            return (mid,True)
        elif (ourlist[mid][0] < key):
            start = mid + 1
        else:
            end = mid - 1
    if (key < ourlist[mid][0]):
        return (mid, False)
    else:
        return (mid + 1, False)

# Use a sorted list
class OurDictionary3():
    def __init__(self):
        self.dict = [('a',12),('c',4),('f',4),('y',134),('z',4)]
    # Use binary search to get the index


    def add_key_value_pair(self, tup):
        for idx, val in enumerate(self.dict):
            if (val[0] > tup[0]):
                self.dict.insert(idx, tup)
                break
        print(self.dict)



# Use open addressing
class HashTable():
    INITIAL_SIZE = 20
    def __init__(self):
        self.array = [None] * self.INITIAL_SIZE

    # Hash function to convert string to a number
    def hash_string(self, mystr):
        a = 676757484
        b = 17
        p = 3571
        m = self.INITIAL_SIZE
        num = 0
        for idx, char in enumerate(mystr):
            num += ord(char) * idx

        myhash = (((a * num) + b) % p) % m
        return myhash
    def hash_string2(self, mystr):
        a = 3636363
        b = 3434
        p = 3571
        m = self.INITIAL_SIZE
        num = 0
        for idx, char in enumerate(mystr):
            num += ord(char) * idx
        myhash = (((a * num) + b) % p) % m
        return myhash
    def add_key_value_pair(self, key, val):
        idx = self.hash_string(key)
        i = 0
        while ((self.array[idx] is not None) and (self.array[idx]) and (self.array[idx][0] != key)):
            idx = (self.hash_string(key) + i * self.hash_string2(key)) % self.INITIAL_SIZE
            i += 1
        self.array[idx] = (key,val)
    def get_value(self, key):
        idx = self.hash_string(key)
        i = 0
        while ((self.array[idx] is not None) and ((self.array[idx] == ()) or (self.array[idx][0] != key))):
            idx = (self.hash_string(key) + i * self.hash_string2(key)) % self.INITIAL_SIZE
            i += 1
        if (self.array[idx] is None):
            raise KeyError
        else:
            return self.array[idx][1]

    def remove_key(self, key):
        idx = self.hash_string(key)
        i = 0
        while ((self.array[idx] is not None) and (self.array[idx][0] != key)):
            idx = (self.hash_string(key) + i * self.hash_string2(key)) % self.INITIAL_SIZE
            i += 1
        # If found, remove the key and leave a tombstone -> ()
        if (self.array[idx][0] == key):
            self.array[idx] = ()


if __name__ == '__main__':
    ht = HashTable()
    ht.add_key_value_pair('test',232)
    print(ht.array)

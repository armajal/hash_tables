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

# od = OurDictionary()
# od.add_key_value_pair('test',12)
# od.remove_key('test')

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

# od2 = OurDictionary2()
# od2.add_key_value_pair('test2',14)
# od2.add_key_value_pair('test2',1343)
# print(od2.get_value('test2'))
# od2.remove_key('test2')


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

if __name__ == '__main__':
    od3 = OurDictionary3()
    # tup_list = [('a', 1), ('c', 1),('d', 1)]
    # print(get_fancy_index(tup_list, "b"))




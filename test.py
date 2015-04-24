import unittest
import main

class TestOurDictionary3(unittest.TestCase):

    def test_get_fancy_index(self):
        self.assertEqual(main.get_fancy_index([], 'a'), (0,False))
        self.assertEqual(main.get_fancy_index([('a',123)], 'a'), (0,True))
        self.assertEqual(main.get_fancy_index([('a',1),('b',3)], 'a'), (0,True))
        self.assertEqual(main.get_fancy_index([('a',1),('b',3)], 'b'), (1,True))
        self.assertEqual(main.get_fancy_index(
          [('a',1),('b',3),('e',232),('g',123),('h',123)], 'e'), 
          (2,True)
        )
        self.assertEqual(main.get_fancy_index(
          [('a',1),('b',3),('e',232),('g',123),('h',123)], 'f'), 
          (3,False)
        )
        self.assertEqual(main.get_fancy_index([('a', 1), ('c', 1),('d', 1)], 'b'), (1,False))


class TestHashTable(unittest.TestCase):

    def test_add_key_value_pair(self):
        ht = main.HashTable()
        ht.add_key_value_pair('test',123)
        self.assertEqual(
            ht.array,
            [None, None, None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, ('test',123)]
            )

    def test_get_value(self):
        ht = main.HashTable()
        ht.add_key_value_pair('test',123)
        self.assertEqual(ht.get_value('test'), 123)


    def test_remove_key(self):
        ht = main.HashTable()
        ht.add_key_value_pair('test',123)
        ht.remove_key('test')
        self.assertEqual(
            ht.array,
            [None, None, None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, ()]            
            )


if __name__ == '__main__':
    unittest.main()
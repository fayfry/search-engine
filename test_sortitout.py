import unittest
import sortitout


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_mormal(self):

        m1 = [6, 8, 9, 9]
        m2 = [1, 3, 9]
        m3 = [2, 4, 7]

        fact = list(sortitout.sortitout([m1, m2, m3]))
        check = [1, 2, 3, 4, 6, 7, 8, 9, 9, 9]

        fact1 =list(sortitout.sortitout([m3, m1, m2]))

        self.assertEqual(fact, check)
        self.assertEqual(fact1, check)

    def test_same(self):

        m1 = [0, 0, 0]
        m2 = [1]

        fact = list(sortitout.sortitout([m1, m2]))
        check = [0, 0, 0, 1]

        fact1 = list(sortitout.sortitout([m2, m1]))

        self.assertEqual(fact, check)
        self.assertEqual(fact1, check)


if __name__ == '__main__':
    unittest.main()

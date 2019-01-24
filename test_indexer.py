from indexer import Position, Index
import unittest
import os
import shelve


class IndexerTest(unittest.TestCase):

    def test_generalindexer(self):

        res = Index().get_index("try2789 to indexate 666please 666work")
        self.assertEqual(len(res), 7)
        self.assertEqual("666" in res, True)
        self.assertEqual("66" in res, False)
        self.assertEqual(res["2789"][0].first_char, 4)
        self.assertEqual(len(res["666"]), 2)

    def test_singlepos(self):

        res = Index().get_index("try")
        dict = {}
        dict.setdefault("try", []).append(Position(1, 3))  # method __eq__
        self.assertEqual(res, dict)
        self.assertEqual(len(res), 1)

    def test_multocc(self):

        res = Index().get_index("try this this and and that")
        self.assertEqual(len(res), 4)
        self.assertEqual(len(res["this"]), 2)
        self.assertEqual(len(res["try"]), 1)
        self.assertEqual(res["try"][0].first_char, 1)
        self.assertEqual(res["try"][0].last_char, 3)
        self.assertEqual(res["this"][0].first_char, 5)
        self.assertEqual(res["this"][1].first_char, 10)

    def test_fileempty(self):

        file = open("test_i1.txt", "w", encoding="utf-8")
        file.close()
        res = Index().get_index_from_file("test_i1.txt")
        os.remove("test_i1.txt")
        self.assertEqual(len(res), 0)

    def test_indfile(self):

        content = ['testing file indexating to', 'or at least pretending to to']
        file = open("test_i2.txt", "w", encoding="utf-8")
        for i in content:
            file.write(i + '\n')
        file.close()

        res = Index().get_index_from_file("test_i2.txt")
        self.assertEqual(len(res["to"]), 3)
        self.assertEqual(len(res["file"]), 1)
        self.assertEqual(res["testing"][0][1].first_char, 1)
        self.assertEqual(res["to"][0][1].first_char, 25)

    def test_emtydb(self):
        file = open("test_i1.txt", "w", encoding="utf-8")
        file.close()
        db = shelve.open("dbtest11", writeback=True)
        Index().indexate_to_db("test_i1.txt", "dbtest11")
        os.remove("test_i1.txt")

        self.assertEqual(len(db), 0)
        db.close()

    def test_db(self):
        content = ['testing file indexating to', 'or at least pretending to to']
        file = open("test_i2.txt", "w", encoding="utf-8")
        for i in content:
            file.write(i + '\n')
        file.close()
        db = shelve.open("dbtest22", writeback=True)
        Index().indexate_to_db("test_i2.txt", "dbtest22")
        os.remove("test_i2.txt")

        self.assertEqual(len(db), 8)
        self.assertEqual(len(db["file"]), 1)
        self.assertEqual(len(db["to"]), 1)
        db.close()


if __name__ == '__main__':
    unittest.main()
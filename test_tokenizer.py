from tokenizer import Tokenizer, Token
import unittest


class TokenizerTest(unittest.TestCase):

    def test_singletoken(self):
        """one token"""
        res = list(Tokenizer().tokenize("first"))
        self.assertEqual(len(res), 1)
        self.assertIsInstance(res[0], Token)
        self.assertEqual(res[0].token, "first")
        self.assertEqual(res[0].first_char, 1)
        self.assertEqual(res[0].last_char, 5)

    def test_nonalph(self):
        """there're non alphabetic symbols"""
        res = list(Tokenizer().tokenize("smth777"))
        self.assertIsInstance(res[0], Token)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[1].token, "777")
        self.assertEqual(res[1].first_char, 5)
        self.assertEqual(res[1].token_type, "d")

    def test_severaltypes(self):
        """several types of tokens in the string"""
        res = list(Tokenizer().tokenize("smth, anyth   "))
        self.assertEqual(len(res), 5)
        self.assertIsInstance(res[0], Token)
        self.assertIsInstance(res[4], Token)
        self.assertEqual(res[0].token, "smth")
        self.assertEqual(res[2].token, " ")
        self.assertEqual(res[2].token_type, "s")
        self.assertEqual(res[4].token_type, "s")


class TokenizerAlphTest(unittest.TestCase):

    def test_notstr(self):
        with self.assertRaises(TypeError):
            Tokenizer().tokenize_alph([",", "568", "ghjhgg"])

    def test_singletoken(self):
        """one token"""
        res = list(Tokenizer().tokenize_alph("first"))
        self.assertEqual(len(res), 1)
        self.assertIsInstance(res[0], Token)
        self.assertEqual(res[0].token, "first")

    def test_nonalph(self):
        """there're non alphabetic symbols"""
        res = list(Tokenizer().tokenize_alph("smth!!!2"))
        self.assertEqual(len(res), 1)

    def test_severaltypes(self):
        """several types of tokens in the string"""
        res = list(Tokenizer().tokenize_alph("smth, anyth   "))
        self.assertEqual(len(res), 2)
        self.assertIsInstance(res[0], Token)
        self.assertIsInstance(res[1], Token)

if __name__ == '__main__':
    unittest.main()

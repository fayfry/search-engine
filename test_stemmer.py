import unittest
from stemmer import Stemmer
from tokenizer import Token, Tokenizer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_stemmer(self):
        line = "мамочка свари суп"
        #tok = Tokenizer().tokenize_alph(line)

        fact = list(Stemmer().stem(Token(0, 7, line, 'a'), 4, line))

        check = [Token(0, 7, line, 'a'), Token(0, 6, line, 'a'),
                 Token(0, 5, line, 'a'), Token(0, 4, line, 'a'), Token(0, 3, line, "a")]

        fact1 = list(Stemmer().stem(Token(14, 17, line, "a"), 4, line))
        check1 = [Token(14, 17, line, "a")]

        self.assertEqual(fact, check)
        self.assertEqual(fact1, check1)

    def test_stemmer_flex(self): 

        line = "мамочка свари суп"

        fact = list(Stemmer().stem_flex(Token(0, 8, "мамочка свари суп", "a")))
        check = [Token(0, 8, line, 'a'), Token(0, 7, line, 'a')]

        self.assertEqual(fact, check)


if __name__ == '__main__':
    unittest.main()

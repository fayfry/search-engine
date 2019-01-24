"""
This module provides stemming functions.
Contains two stemmers of different complexity,the first one generates pseudo-stemms
and flexions of a fixed length and the second one takes real flexions of the russian
language into consideration
"""


from tokenizer import Token, Tokenizer


class Stemmer(object):

    def __init__(self, file="flex.txt"):

        with open(file, "r", encoding="utf-8") as file:
            self.flexions = set()
            self.max_len = 1

            for i, line in enumerate(file):
                self.flexions.add(line[:-1])

                if self.max_len < len(line):
                    self.max_len = len(line)-1   #to del "/n" t the end

    def stem(self, word, numletters, line):
        """
        This stemmer takes a Token, a maximum flexion length and a line that
        Token belongs to as the input value and yields all the possible stemms for the word
        """

        length = word.last_char - word.first_char

        if length <= numletters:
            yield word

        else:
            for i in range(0, numletters+1):
                yield Token(word.first_char-1, word.last_char-i, line, "a")

    def stem_flex(self, token):  #должен брать токен
        """This stemmer takes a line and and a list of the russian stemms
         and its max length as the input value and yields all the possible
         stemms for the word"""

        length = token.last_char - token.first_char+1

        if length <= self.max_len:
            yield token.token
            #res.append(token.token)

        else:
            for i in range(0, self.max_len):
                if i == 0:
                    yield token.token
                    #res.append(token.token)
                if token.token[-i:] in self.flexions:
                    yield token.token[:-i]
                    #res.append(token.token[:-i])


if __name__ == "__main__":
    #res = list(Stemmer().stem(Token(0, 8, "коровища мыла рану", "a"), 3, "коровища мыла рану"))
    #print(res)

    #flexions = Stemmer().find_flex("flex.txt")[0]
    #max_len = Stemmer().find_flex("flex.txt")[1]
    #print(flexions)
    print(Stemmer().stem_flex(Token(0, 8, "коровища мыла рану", "a")))

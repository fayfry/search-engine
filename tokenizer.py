"""
Module for tokenizing. Methods work with string objects
"""

import unicodedata


class Token(object):
    """
    Class for storing tokens w/ their first/last chars and types
    """
    def __init__(self, first_char, last_char, line, token_type):

        self.first_char = first_char+1
        self.last_char = last_char
        self.token = line[first_char:last_char]
        self.token_type = token_type

    def __repr__(self):

        return "{0}: [{1}, {2}]".format(self.token, self.first_char, self.last_char)

    def __eq__(self, other):
        if (self.first_char == other.first_char and
            self.last_char == other.last_char and
            self.token == other.token and
            self.token_type == other.token_type):
            return True
        else:
            return False



class Tokenizer(object):
    """
    Class for tokenizing methods
    """
    def tokenize_alph(self, line):
        """
        Method tokenize_alph gets an input line and returns alphabetical
        tokens with their characteristics (first/last chars, type)
        as a list

        :param line: input string object
        :return: list of tokens with their attributes
        """

        if not isinstance(line, str):
            raise TypeError("I can't work with it! Give me a string object")

        inside = False
        tokenized_line = []

        for i, char in enumerate(line):
            if char.isalpha():
                if not inside:
                    first_char = i
                    inside = True
            elif inside:
                tokenized_line.append(Token(first_char, i, line, "a"))
                inside = False

        if line != "" and line[-1].isalpha():  #to add the last token in the line
            tokenized_line.append(Token(first_char, i + 1, line, "a"))

        return tokenized_line

    def tokenize(self, line):
        """
        Method tokenize gets an input line and returns tokens
        with their characteristics (first/last chars, type)
        as a list generator
        :param line: input string object for tokenizing
        :return: generator object that yields token with its attributes
        """

        if not isinstance(line, str):
            raise TypeError("I can't work with it! Give me a string object")

        token_type = None
        first_char = None

        for i, char in enumerate(line):
            new_token = Tokenizer().check(char)
            if new_token != token_type:
                if token_type is not None:
                    token = Token(first_char, i, line, token_type)
                    yield token
                first_char = i
            token_type = new_token

        if line != "":  # to add the last token
            token = Token(first_char, i+1, line, token_type)
        yield token

    @staticmethod
    def check(char):
        """
        Method check returns type of the current token:
        alphabetical, digital, space or punctuation
        :param char:
        :return: token type as a string:
                "a" - alphabetical
                "d" - digital
                "s" - space
                "p" - punctuational
        """

        token_type = None
        if char.isalpha():
                token_type = "a"
        if char.isdigit():
            if token_type != "d":
                token_type = "d"
        if char.isspace():
            if token_type != "s":
                token_type = "s"
        if not (char.isspace() or char.isalpha() or char.isdigit()):
            category = unicodedata.category(char)
            if category[0] == "P":
                if token_type != "p":
                    token_type = "p"
        return token_type
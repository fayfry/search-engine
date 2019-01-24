"""
Module for indexating strings, files and storing the indices into a data base
"""

from tokenizer import Tokenizer
import shelve


class Position(object):
    """
    Class that stores info about token positions
    """
    def __init__(self, first_char, last_char):
        self.first_char = first_char
        self.last_char = last_char

    def __repr__(self):
        return "{0}:{1}".format(self.first_char, self.last_char)

    def __eq__(self, other):
        if self.first_char == other.first_char and self.last_char == other.last_char:
            return True
        else:
            return False


class PositionInFile(Position):
    """
    Class that stores info about token positions got from a file
    """
    def __init__(self, first_char, last_char, line):
        self.first_char = first_char
        self.last_char = last_char
        self.line = line

    def __repr__(self):
        return "{0}:{1} line {2}"\
            .format(self.first_char, self.last_char, self.line)

    def __eq__(self, other):
        if (self.first_char == other.first_char and
            self.last_char == other.last_char and
            self.line == other.line):
            return True
        else:
            return False

    def __lt__(self, other):
        if self.line != other.line:
            return self.line < other.line
        elif self.first_char != other.first_char:
            return self.first_char < other.first_char
        else:
            return self.last_char < other.last_char


class Index(object):
    """
    Class for indexating strings
    """
    def get_index(self, input):
        """Get indices

        Method get_index creates dictionary where keys are tokens
        and values are their positions (first/last chars) as a list
        :param input:
        :return:
        """
        dict = {}
        for i in Tokenizer().tokenize(input):
            if i.token_type == "a" or i.token_type == "d":
                dict.setdefault(i.token, [])\
                    .append(Position(i.first_char, i.last_char))
        return dict

    def get_index_from_file(self, file):
        """Get indices from a file

        Method get_index_from_file creates dictionary where keys are tokens,
        values are their positions (first/last chars, path, line)
        as a list
        :param file:
        :return:
        """

        self.file = file
        dict = {}
        with open(file, 'r') as file:
            for i, line in enumerate(file):
                for j in Tokenizer().tokenize(line):
                    if j.token_type == "a" or j.token_type == "d":
                        list = [file.name, PositionInFile(j.first_char, j.last_char, i+1)]
                        dict.setdefault(j.token, []).append(list)
        return dict

    def indexate_to_db(self, tom, data):
        """Store indices into data base

        :param file:
        :return:
        """
        self.data = data
        self.tom = tom

        t = Tokenizer()
        with open(tom, 'r') as file:
            db = shelve.open(data, writeback=True)

            for i, line in enumerate(file):
                res = t.tokenize(line)
                for j in res:
                    if j.token_type == "a" or j.token_type == "d": # метод у токенизатора
                        e = j.token
                        x = db.setdefault(e, {})
                        x.setdefault(file.name, []).append(PositionInFile(j.first_char, j.last_char, i + 1))
                        #  db[e] = x
            db.close()


if __name__ == "__main__":
    Index().indexate_to_db('tom1.txt', 'database')
    print('done')
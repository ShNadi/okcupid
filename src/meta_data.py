"""
This page contains functions for preprocessing OkCupid dataset.

"""
import string
import readability
from textblob import TextBlob
from spellchecker import SpellChecker
from tqdm import tqdm
tqdm.pandas()


class Stylo():
    """
    Class contains methods for calculating specific linguistic features from text.

    """

    def count_char(self, s):
        """
        Count the number of characters in a given string.

        :return: count number of characters for sting s
        :rtype: int
        """
        count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
        s_chars = count(s, string.ascii_letters)
        return s_chars

    def count_punc(self, s):
        """
        Count the number of punctuations in a given string.

        :return: count number of punctuations for string s
        :rtype: int
        """
        count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
        s_punct = count(s, string.punctuation)
        return s_punct

    def count_words(self, s):
        """
        Count the number of words in a given string.

        :return: count number of words for string s
        :rtype: int
        """
        s_words = s.split()
        return len(s_words)

    def count_spellerror(self, s):
        """
        Count the number of misspelled words in a given sting.

        :return: count number of misspelled words for string s
        :rtype: int
        """
        tb = TextBlob(s)
        words = tb.words
        spell = SpellChecker()
        misspelled = spell.unknown(words)
        return misspelled

    def text_readability(self, text):
        """
        Calculate the readability for a given text.

        :return: readability measure
        :rtype: float
        """
        results = readability.getmeasures(text, lang='en')
        return results['readability grades']['FleschReadingEase']

    def uniqueness(self, s):
        """
        Calculate the uniqueness of words in a given sting.

        :param s: original text
        :type s: sting
        :return: uniqueness degree
        :rtype: float
        """
        b = s.split()
        myset = set(b)
        uniq_len = len(myset)
        no_words = len(b)
        avg_uniq = round((uniq_len / no_words), 2)
        return avg_uniq
"""
This page contains functions for pre_processing OkCupid data_set.

It seems that it has to have THIS docstring with a summary line, a blank line
and some more text like here. Wow.
"""
import string
import readability
from textblob import TextBlob
from spellchecker import SpellChecker
from tqdm import tqdm
tqdm.pandas()


class Stylo():
    """
    Class contains methodes for calculating user specific features of text.

    """

    def count_char(self, s):
        """
        Count the number of characters in a given string.

        :return: count number of characters for sting s
        :rtype: int
        """
        count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
        s_chars = count(s, string.ascii_letters)
        return s_chars

    def count_punc(self, s):
        """
        Count the number of punctuations in a given string.

        :return: count number of punctuations for string s
        :rtype: int
        """
        count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
        s_punct = count(s, string.punctuation)
        return s_punct

    def count_words(self, s):
        """
        Count the number of words in a given string.

        :return: count number of words for string s
        :rtype: int
        """
        s_words = s.split()
        return len(s_words)

    def count_spellerror(self, s):
        """
        Count the number of misspelled words in a given sting.

        :return: count number of misspelled words for string s
        :rtype: int
        """
        tb = TextBlob(s)
        words = tb.words
        spell = SpellChecker()
        misspelled = spell.unknown(words)
        return misspelled

    def text_readability(self, text):
        """
        Calculate the readability for a given text.

        :return: readability measure
        :rtype: float
        """
        results = readability.getmeasures(text, lang='en')
        return results['readability grades']['FleschReadingEase']

    def uniqueness(self, s):
        """
        Calculate the uniqueness of words in a given sting.

        :param s: original text
        :type s: sting
        :return: uniqueness degree
        :rtype: float
        """
        b = s.split()
        myset = set(b)
        uniq_len = len(myset)
        no_words = len(b)
        avg_uniq = round((uniq_len / no_words), 2)
        return avg_uniq

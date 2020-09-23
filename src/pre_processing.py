"""
This page contains functions for preprocessing OkCupid data_set.

"""
import pandas as pd
import nltk
from termcolor import colored
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import string
from string import punctuation
from sklearn.feature_extraction import stop_words
pd.set_option('display.expand_frame_repr', False)


class PreProcess():
    """
    This page contains functions for preprocessing OkCupid dataset.

    """

    def __init__(self):
        pass

    def missing_value(self, df):
        """
        Removes dataset rows that have all null or education column
        or essay columns are null.

        :param df: Original dataset
        :type df: DataFrame
        :return: dataSet without null values in essays and education columns
        :rtype: DataFrame
        """
        print('\033[1m \033[94m Original dataset shape:\033[0m \033[0m {}\n'.format(df.shape))
        # drop rows with all null values
        df = df.dropna(axis='rows', how='all')
        print('\033[1m \033[94m Shape of dataset after dropping the rows containing all null values:\033[0m \033[0m {}\n'.
            format(df.shape))

        # drop rows in which the education field is empty
        df = df.dropna(subset=['education'])
        print(
            '\033[1m \033[94m Shape of dataset after dropping the rows with null value in education:\033[0m \033[0m {}'
            '\n'.format(df.shape))

        # drop rows in which all the essay fields are empty
        df = df.dropna(subset=['essay0', 'essay1', 'essay2', 'essay3', 'essay7', 'essay8', 'essay9'], how='all')
        print(
            '\033[1m \033[94m Shape of dataset after dropping the rows with all null values in essays:\033[0m \033[0m '
            '{}\n'.format(df.shape))
        return df

    def merge_essay(self, df):
        """
        Merges the essayes number 0, 1, 2, 3, 7, 8, 9 as a sinigle text.

        :param df: Original dataset
        :type df: DataFrame
        :return: dataframe including joint texts
        :rtype: DataFrame
        """

        df['text'] = df['essay0'].fillna('') + ' ' + df['essay1'].fillna('') + ' ' + df['essay2'].fillna('') + ' ' + df[
            'essay3'].fillna('') + ' ' + df['essay7'].fillna('') + ' ' + df['essay8'].fillna('') + ' ' + df[
                         'essay9'].fillna('')
        print(colored('essays are merged now!', 'green'))
        return df

    def remove_tag(self, df):
        """
        Removes htmls tags and newlines.

        :param df: Original dataset
        :type df: DataFrame
        :return: df text without html tags and newlines
        :rtype: DataFrame
        """
        df['text'] = df['text'].replace('<[^<]+?>', '', regex=True)
        df['text'] = df['text'].replace("\n", "", regex=True)
        print(colored('html tags are removed!', 'green'))
        return df

    def count_words_sentences(self, df):
        """
        Calculates the avarage number of words per sentence

        :param df: Original dataset
        :type df: DataFrame
        :return: df including new column named #anwps
        :rtype: DataFrame
        """
        df = df.dropna(subset=['text'])
        # split text to words
        df['words'] = df.apply(lambda row: nltk.word_tokenize(row['text']), axis=1)
        # number of words in for each user
        df['#words'] = df.apply(lambda row: len(row['words']), axis=1)
        print(colored('number of words is calculated...', 'green'))

        # split text to sentences
        df['sentences'] = df.apply(lambda row: nltk.sent_tokenize(row['text']), axis=1)
        # number of sentences for each user
        df['#sentences'] = df.apply(lambda row: len(row['sentences']), axis=1)
        print(colored('number of sentences is calculated...', 'green'))

        # avarage number of words per sentence
        df['#anwps'] = df.apply(lambda row: row['#words'] / row['#sentences'], axis=1)
        print(colored('average number of words per sentence is calculated...', 'green'))
        # return df
        return df

    def recode_edcuaction(self, df):
        """
        Recode eduction variable in OK cupid data to ISCED 2011 code.

        Level 	ISCED 2011
        # 0	Early childhood Education (01 Early childhood educational development)
        # 1	Primary education
        # 2	Lower secondary education
        # 3	Upper secondary education
        # 4	Post-secondary non-tertiary education
        # 5	Short-cycle tertiary education
        # 6	Bachelor or equivalent
        # 7	Master or equivalent
        # 8	Doctoral or equivalent

        # see also:
        # https://en.wikipedia.org/wiki/
        #International_Standard_Classification_of_Education#ISCED_2011_levels,
        # _categories,_and_sub-categories

        :param dic: a dictionary
        :param df: data_set containing the column we need to recode
        :return: returns the data_frame containing recoded column
        """
        dic = {
            "graduated from college/university": "6",
            "graduated from masters program": "7",
            "working on college/university": "3",
            "working on masters program": "6",
            "graduated from two-year college": "5",
            "graduated from high school": "3",
            "graduated from ph.d program": "8",
            "graduated from law school": "8",
            "working on two-year college": "3",
            "dropped out of college/university": "3",
            "working on ph.d program": "7",
            "college/university": "6",
            "graduated from space camp": "-1",
            "dropped out of space camp": "-1",
            "graduated from med school": "8",
            "working on space camp": "-1",
            "working on law school": "7",
            "two-year college": "3",
            "working on med school": "7",
            "dropped out of two-year college": "3",
            "dropped out of masters program": "6",
            "masters program": "6",
            "dropped out of ph.d program": "7",
            "dropped out of high school": "1",
            "high school": "3",
            "working on high school": "1",
            "space camp": "-1",
            "ph.d program": "7",
            "law school": "8",
            "dropped out of law school": "7",
            "dropped out of med school": "7",
            "med school": "8",
        }

        df['isced'] = df['education']
        df = df.replace(dict(isced=dic))
        df.isced[df['isced'] == '-1'] = None
        df.dropna(subset=['isced'])
        print(colored('education column is coded...', 'green'))

        inv_dic = {
            '0':'Early childhood Education',
            '1': 'Primary education',
            '2': 'Lower secondary education',
            '3': 'Upper secondary education',
            '4': 'Post-secondary non-tertiary education',
            '5': 'Short-cycle tertiary education',
            '6': 'Bachelor or equivalent',
            '7': 'Master or equivalent',
            '8': 'Doctoral or equivalent',
        }

        df['isced2'] = df['isced']
        df = df.replace(dict(isced2=inv_dic))
        # df.isced[df['isced2'] == '-1'] = "None"
        df.dropna(subset=['isced2'])
        print(colored('education column is coded again...', 'green'))


        return df

    def text_cleaning(self, df):
        # Remove punctuations
        def remove_punctuation(s):
            s = ' '.join([i for i in s if i not in frozenset(string.punctuation)])
            return s

        df['removed_punctuation'] = df.apply(lambda x: remove_punctuation(x['text']), axis=1)

        # Remove stopwords
        def remove_stopwords(text):
            stopword_list = stop_words.ENGLISH_STOP_WORDS
            text = ' '.join([word for word in text.split() if word not in stopword_list])
            return text

        df['removed_stopwords'] = df.apply(lambda x: remove_stopwords(x['removed_punctuation']), axis=1)

        # Remove numbers
        df.removed_stopwords = df.removed_stopwords.str.replace('\d+', '')
        df.dropna(subset=['removed_stopwords'])
        df.rename(columns={'removed_stopwords': 'clean_text'}, inplace=True)

        print(colored('text is clean...', 'green'))
        return df

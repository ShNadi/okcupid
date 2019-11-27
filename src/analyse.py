import pandas as pd


class Analyse():
    """
    This page contains functions for pre_processing OkCupid data_set.

    It seems that it has to have THIS docstring with a summary line,
    a blank line.
    and some more text like here. Wow.
    """

    def __init__(self):
        pass

    def sumary(self, df):
        return df.describe()


# cupid_df = pd.read_csv('../data/processed/preprocessed_cupid.csv', usecols = ['education', 'age', 'sex', 'text',
#                                 'isced', '#words', '#sentences', '#anwps', 'removed_stopwords'])
# cupid_df.rename(columns={'removed_stopwords': 'clean_text'}, inplace=True)
# a = Analyse()
# print(a.sumary(cupid_df))
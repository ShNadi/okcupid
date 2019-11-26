
"""
This page contains functions for pre_processing OkCupid data_set.

It seems that it has to have THIS docstring with a summary line, a blank line
and some more text like here. Wow.
"""
import pandas as pd


pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv("../data/raw/profiles.csv")
# print(df)

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


def recode_edcuaction(dic, df):
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
    df['isced'] = df['education']
    df = df.replace(dict(isced=dic))
    df.isced[df['isced'] == '-1'] = "None"

    return df


# df = recode_edcuaction(dic, df)
# print(df.isced)

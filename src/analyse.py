import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from termcolor import colored
from wordcloud import WordCloud

sns.set(color_codes=True)


class Analyse():
    """
    This page contains functions for pre_processing OkCupid data_set.

    It seems that it has to have THIS docstring with a summary line,
    a blank line.
    and some more text like here. Wow.
    """

    def __init__(self):
        pass

    def summary(self, df):
        return df.describe()

    def plot_func(self, df, type='#anwps_freq', sex=False):
        if type == '#anwps_freq':
            # Plot histogram for avarage number of words per sentence
            sns.distplot(df["#anwps"], kde=False).set_title(
                "Histogram of of avarage number of words per sentence")
            plt.show()

        elif type == 'isced_freq' and sex:
            # Plot frequency of participants based on their
            #  sex and level of education
            df.groupby(['sex']).isced2.value_counts().unstack(0).plot.barh(figsize=(10, 10))
            plt.title("Frequency of participants based of their sex and level of education")
            plt.show()
        elif type == 'isced_freq' and not sex:
            n = df.shape[0]
            df = df.groupby('isced').count() / n
            df.sort_values(['#anwps'], ascending=False, inplace=True)

            df['#anwps'].plot(kind='bar')
            plt.title("Frequency of participants based on their level of education")
            plt.show()

        elif type == 'boxplot' and not sex:
            # Create a boxplot
            sns.boxplot(df["#anwps"]).set_title("Boxplot of the average number of words per sentence")
            plt.show()

        elif type == 'boxplot' and sex:
            # Plot boxplot of #anwps for men and women
            df.groupby(['sex'])['#anwps'].value_counts().unstack(0).boxplot(figsize=(10, 10))
            plt.title("Boxplot of the average number of words per sentence for men and women")
            plt.show()

        elif type == 'common_words':
            df = df.dropna(subset=['clean_text'])
            top = Counter(" ".join(df["clean_text"]).split()).most_common(30)
            top = top[::-1]
            x, frequency = zip(*top)

            x_pos = [i for i, _ in enumerate(x)]
            # x_pos.reverse()

            plt.barh(x_pos, frequency, color='green')
            plt.ylabel("Frequent word")
            plt.xlabel("Word frequency")
            plt.title("Top 30 common words")
            plt.yticks(x_pos, x)
            plt.show()

        elif type == 'word_cloud':
            # Plot wordcloud of 100 most frequent words
            wordcloud = WordCloud(
                width=3000,
                height=2000,
                background_color='black',
                max_words=100
            ).generate(str(df["clean_text"]))
            fig = plt.figure(
                figsize=(10, 7.5),
                facecolor='k',
                edgecolor='k')
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.tight_layout(pad=0)
            plt.title("Wordcloud of 100 most frequent words")
            plt.show()

        elif type == 'age_sex':
            # Plot frequency of participants based of their sex and age
            df.groupby(['age']).sex.value_counts().unstack(0).plot.barh(figsize=(10, 10))
            plt.title("Frequency of participants based of their sex and age")
            plt.show()

        else:
            print(colored('please select a valid type for plot!', 'red'))


if __name__ == "__main__":
    cupid_df = pd.read_csv('../data/processed/preprocessed_cupid.csv',
                           usecols=['education',
                                    'age',
                                    'sex',
                                    'text',
                                    'isced',
                                    '#words',
                                    '#sentences',
                                    '#anwps',
                                    'removed_stopwords'])
    cupid_df.rename(columns={'removed_stopwords': 'clean_text'}, inplace=True)
    a = Analyse()
    a.plot_func(cupid_df, type='word_cloud')

"""
This page contains functions for pre_processing OkCupid data_set.

"""
import pre_processing
import analyse
import meta_data
import classify
import pandas as pd
from termcolor import colored


def main_func(pprocess=False, analyze=False, meta=False, classification=False,
              func='summary_stat', type='#anwps_freq', sex=False, age=False):

    # Do pre_processing task
    if(pprocess):
        # Read data_set with limited columns
        cupid_df = pd.read_csv('../data/raw/profiles.csv', usecols=[
            'education', 'essay0', 'essay1', 'essay2', 'essay3', 'essay7',
            'essay8', 'essay9', 'age', 'sex'])

        # Define an object of pre_processing class
        cupid = pre_processing.PreProcess()

        cupid_df = cupid.missing_value(cupid_df)
        cupid_df = cupid.merge_essay(cupid_df)
        cupid_df = cupid.remove_tag(cupid_df)
        cupid_df = cupid.recode_edcuaction(cupid_df)
        cupid_df = cupid.count_words_sentences(cupid_df)
        cupid_df = cupid.text_cleaning(cupid_df)

        # Save pre_processed dat_set on disk
        cupid_df.to_csv(r'../data/processed/preprocessed_cupid.csv',
                        index=None, header=True)

        # Final message
        print(colored('preprocessed_cupid.csv is written in data/preprocessed\
         folder...', 'red'))

    # ************************************************************************
    # Do analyses task
    elif(analyze):
        # Read pre_processed data_set with limited columns
        cupid_dfa = pd.read_csv(
            '../data/processed/preprocessed_cupid.csv',
            usecols=['education', 'age', 'sex', 'text', 'isced', 'isced2',
                     '#words', '#sentences', '#anwps', 'clean_text'])
        # cupid_dfa.rename(columns={'removed_stopwords': 'clean_text'},
        # inplace=True)

        # Define an object of pre_processing class
        a_cupid = analyse.Analyse()

        if (func == 'summary_stat'):
            summary_df = a_cupid.summary(cupid_dfa)
            summary_df.to_json(r'../results/figures/summary_statistics.json')
            summary_df.to_csv(r'../results/figures/summary_statistics.csv')
            print(colored('summary_statistics.csv is written in '
                          'results/figure folder...', 'magenta'))
        elif (func == 'plot'):
            a_cupid.plot_func(cupid_dfa, type, sex)

    # *************************************************************************
    # Calculate meta_data
    if(meta):
        style = meta_data.Stylo()
        # Read data_set
        df_preprocessed = pd.read_csv(
            '../data/processed/preprocessed_cupid.csv',
            usecols=['age', 'sex', '#anwps', 'clean_text', "text",
                     'isced', 'isced2'])

        df_preprocessed.dropna(subset=['text', 'isced'], inplace=True)

        # Print the progress number
        print(colored('\nCalculating count_char:\n', 'green'))
        df_preprocessed['count_char'] = df_preprocessed.progress_apply(
            lambda x: style.count_char(x['text']), axis=1)

        # Print the progress number
        print(colored('\nCalculating count_punct:\n', 'green'))
        df_preprocessed['count_punct'] = df_preprocessed.progress_apply(
            lambda x: style.count_punc(x['text']), axis=1)

        # df_preprocessed['count_digit'] = sum(c.isdigit() for c in
        #                                      df_preprocessed['text'])

        # Print the progress number
        print(colored('\nCalculating count_word:\n', 'green'))
        df_preprocessed['count_word'] = df_preprocessed.progress_apply(
            lambda x: style.count_words(x['text']), axis=1)

        # Print the progress number
        print(colored('\nCalculating avg_wordlength:\n', 'green'))
        df_preprocessed['avg_wordlength'] = round(df_preprocessed[
            'count_char'] / df_preprocessed['count_word'], 2)

        # Print the progress number
        print(colored('\nCalculating count_misspelled:\n', 'green'))
        df_preprocessed['count_misspelled'] = \
            df_preprocessed.progress_apply(lambda x:
                                           style.count_spellerror(x[
                                               'text']), axis=1)

        # df_preprocessed['readability'] = df_preprocessed.progress_apply(
        #     lambda x: style.text_readability(x['text']), axis=1)

        # Print the progress number
        print(colored('\nCalculating words uniqueness:\n', 'green'))
        df_preprocessed['word_uniqueness'] = df_preprocessed.progress_apply(
            lambda x: style.uniqueness(x['text']), axis=1)

        # Save calculated meta_data on disk
        df_preprocessed.to_csv(r'../data/processed/stylo_cupid_test.csv',
                               index=None, header=True)

        # Final message
        print(colored('stylo_cupid.csv is written in data/preprocessed\
                 folder...', 'red'))

    # **************************************************************************
    if(classification):
        cls = classify.Classifier()
        df_cls = pd.read_csv(r'../data/processed/stylo_cupid2.csv')
        cls.logistic_text_meta(df_cls)



"""
    Main function:

    -- set pprocess=True for doing pre_processing
        --- pre_processing includes:
            ---- checking missing values
            ---- merging essays as a unique text
            ---- removing stop words
            ---- removing html tags
            ---- recoding education feature
            ---- removing punctuation
            ---- count the number of sentences and words
        the pre_processing function writes the preprocessed data set as
        csv file in 'data/preprocessed' path.

    -- set analyze=False and func='summary_stat':
        --- writes statistical summary of data set as a csv and json file
        in 'results/figures'
    -- set analyze=True, func=plot and:
        --- type='#anwps_freq' to draw plot of average number of words per
        sentence
        --- type='isced_freq' and sex=True to draw plot of frequency of
        participants based of their sex and level of education
        --- type='isced_freq' and sex=False to draw plot of overall
        frequency of participants based on level of education
        --- type='boxplot' and sex=False to draw boxplot of the average
        number of words per sentence
        --- type='boxplot' and sex=True to draw boxplot of the average
        number of words per sentence for male and female
        --- type='common_words' to draw bar chart of top 30 common words
        --- type='word_cloud' to draw word cloud of 100 most frequent words
        --- type='age_sex' to draw plot of frequency of participants based
        of their sex and age

    -- set meta_data=True for calculating user specific features
        ---
"""
if __name__ == "__main__":
    main_func(pprocess=True)
    main_func(analyze=False, func='plot', type='isced_freq', sex=False)
    # main_func(analyze=False, func='plot', type='sex_age')
    main_func(meta=False)
    main_func(classification=False)


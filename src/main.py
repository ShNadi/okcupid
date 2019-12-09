import pre_processing
import analyse
import pandas as pd
from termcolor import colored


def main_func(pprocess=False, analyze=False, func='summary_stat', type='#anwps_freq', sex=False, age=False):
    if(pprocess==True):
        cupid_df = pd.read_csv('../data/raw/profiles.csv', usecols = ['education', 'essay0', 'essay1', 'essay2',
                                                                      'essay3', 'essay7', 'essay8', 'essay9', 'age', 'sex'])
        cupid = pre_processing.PreProcess()

        cupid_df = cupid.missing_value(cupid_df)
        cupid_df = cupid.merge_essay(cupid_df)
        cupid_df = cupid.remove_tag(cupid_df)
        cupid_df = cupid.recode_edcuaction(cupid_df)
        cupid_df = cupid.count_words_sentences(cupid_df)
        cupid_df = cupid.text_cleaning(cupid_df)
        export_csv = cupid_df.to_csv (r'../data/processed/preprocessed_cupid.csv', index = None, header=True)
        print(colored('preprocessed_cupid.csv is written in data/preprocessed folder...', 'red'))

    elif(analyze==True):

        cupid_dfa = pd.read_csv('../data/processed/preprocessed_cupid.csv', usecols = ['education', 'age', 'sex', 'text',
                                'isced', '#words', '#sentences', '#anwps', 'clean_text'])
        # cupid_dfa.rename(columns={'removed_stopwords': 'clean_text'}, inplace=True)
        a_cupid = analyse.Analyse()
        if func=='summary_stat':
            summary_df = a_cupid.summary(cupid_dfa)
            summary_df.to_json(r'../results/figures/summary_statistics.json')
            summary_df.to_csv(r'../results/figures/summary_statistics.csv')
            print(colored('summary_statistics.csv is written in results/figure folder...', 'magenta'))
        elif func=='plot':
            a_cupid.plot_func(cupid_dfa, type, sex)




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
        the pre_processing function writes the preprocessed data set as csv file in 'data/preprocessed' path
        
    -- set analyze=False and func='summary_stat':
        --- writes statistical summary of data set as a csv and json file in 'results/figures'
    -- set analyze=True, func=plot and:
        --- type='#anwps_freq' to draw plot of average number of words per sentence
        --- type='isced_freq' and sex=True to draw plot of frequency of participants based of their sex and level of education
        --- type='isced_freq' and sex=False to draw plot of overall frequency of participants based on level of education
        --- type='boxplot' and sex=False to draw boxplot of the average number of words per sentence
        --- type='boxplot' and sex=True to draw boxplot of the average number of words per sentence for male and female
        --- type='common_words' to draw bar chart of top 30 common words
        --- type='word_cloud' to draw word cloud of 100 most frequent words
"""

main_func(pprocess=False)
main_func(analyze=True, func='plot', type='isced_freq', sex=False)
main_func(analyze=False, func='plot', type='sex_age')


# TODO: add list of education levels
# TODO: documentation

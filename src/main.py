import pre_processing
import analyse
import pandas as pd
from termcolor import colored


def main_func(pprocess=False, analyze=False, func='summary_stat', type='#anwps_freq', sex=False):
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





main_func(pprocess = False)
main_func(analyze = True, func='plot', type = 'isced', sex=False)



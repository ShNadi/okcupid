import pre_processing
import pandas as pd


cupid_df = pd.read_csv('../data/processed/preprocessed_cupid.csv')
# cupid_df = pd.read_csv('D:/Github/OkCupid/Data/profiles.csv', usecols = ['education', 'essay0', 'essay1', 'essay2', 'essay3',
#                                                                    'essay7', 'essay8', 'essay9', 'age', 'sex'])



#
# cupid = pre_processing.PreProcess()
# cupid_df = cupid.missing_value(cupid_df)
# cupid_df = cupid.merge_essay(cupid_df)
# cupid_df = cupid.remove_tag(cupid_df)
# cupid_df = cupid.recode_edcuaction(cupid_df)
# cupid_df = cupid.count_words_sentences(cupid_df)
# cupid_df = cupid.text_cleaning(cupid_df)
# export_csv = cupid_df.to_csv (r'../data/processed/preprocessed_cupid.csv', index = None, header=True)
print(cupid_df)

"""
This page contains implementation of classifier class.

Before training logistic regression model:
1- Merge ISCD levels 1,3,5 as primary education and 6,7, 8 as higher education
2- Join metadata to clean_text dataset
3- classify based on joint model
"""
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion
from collections import Counter
import numpy as np
import itertools


class Classifier():
    """
    This class uses logistic regression classifier.

    two approaches are considered:
    1- classify based on text only
    2- classify based on text and metadata
    """

    def plot_confusion_matrix(self, cm, classes, normalize=False,
                              title='Confusion matrix', cmap=plt.cm.Blues):
        """
        Print and plots the confusion matrix.

        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    def logistic_text_meta(self, df):
        df['sex'].mask(df['sex'].isin(['m']), 0.0, inplace=True)
        df['sex'].mask(df['sex'].isin(['f']), 1.0, inplace=True)
        # print(df['sex'].value_counts())

        df['isced'].mask(df['isced'].isin([3.0, 5.0]), 1.0, inplace=True)
        df['isced'].mask(df['isced'].isin([6.0, 7.0]), 8.0, inplace=True)

        print(sorted(Counter(df['isced']).items()))
        df = df.dropna(subset=['clean_text', 'isced'])

        corpus = df[['clean_text', 'count_char', 'count_word', '#anwps',
                     'count_punct', 'avg_wordlength', 'count_misspelled',
                     'word_uniqueness', 'age', 'sex']]
        target = df["isced"]

        # vectorization
        X_train, X_val, y_train, y_val = train_test_split(corpus, target,
                                                          train_size=0.75,
                                                          test_size=0.25,
                                                          random_state=0)

        get_text_data = FunctionTransformer(lambda x: x['clean_text'],
                                            validate=False)
        get_numeric_data = FunctionTransformer(lambda x: x[
            ['count_char', 'count_word', '#anwps', 'count_punct',
             'avg_wordlength', 'count_misspelled', 'word_uniqueness',
             'age', 'sex']].astype(float), validate=False)

        # merge vectorized text data and scaled numeric data
        process_and_join_features = Pipeline([
            ('features', FeatureUnion([
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('scaler', preprocessing.StandardScaler())

                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vec',
                     CountVectorizer(binary=False, ngram_range=(1, 2),
                                     lowercase=True))
                ]))
            ])),
            ('clf', LogisticRegression(random_state=0, max_iter=1000,
                                       solver='lbfgs', penalty='l2',
                                       class_weight='balanced'))
        ])

        # merge vectorized text data and scaled numeric data
        process_and_join_features.fit(X_train, y_train)
        predictions = process_and_join_features.predict(X_val)

        print("Final Accuracy for Logistic: %s" % accuracy_score(
            y_val, predictions))
        cm = confusion_matrix(y_val, predictions)
        plt.figure()
        self.plot_confusion_matrix(
            cm, classes=[0, 1], normalize=False, title='Confusion Matrix')
        print(classification_report(y_val, predictions))

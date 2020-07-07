"""
description
"""

# imports
from sklearn.datasets import make_classification
from Evaluator import Evaluator
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def dataset():
    return make_classification(random_state=1410)


def test_evaluator():
    X, y = dataset()

    gnb_clf = GaussianNB()
    knc_clf = KNeighborsClassifier()
    dtc_clf = DecisionTreeClassifier()

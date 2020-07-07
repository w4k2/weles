"""
description
"""

# imports
from sklearn.datasets import make_classification
import Evaluator
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def dataset():
    return make_classification(random_state=1410)


def test_evaluator():
    X, y = dataset()

    gnb_clf = GaussianNB()
    knc_clf = KNeighborsClassifier()
    dtc_clf = DecisionTreeClassifier()
    metrics = {"Accuracy": accuracy_score}
    ev = Evaluator(datasets=dataset)
    clfs = {"GNB classifier": gnb_clf,
            "KNC classifier": knc_clf,
            "DTC classifier": dtc_clf}
    ev.process(clfs=clfs)
    ev.score(metrcis=metrics)

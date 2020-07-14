"""
description
"""

# imports
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import weles as ws

datasets = {
    "jeż": make_classification(random_state=1410, n_samples=2000),
    "kot": make_classification(random_state=1994, n_samples=2000),
    "lis": make_classification(random_state=1989, n_samples=2000),
    "byk": make_classification(random_state=1992, n_samples=2000,
                               weights=(.9, .1))
}
metrics = {
    "accuracy": accuracy_score,
    "balanced accuracy score": ws.metrics.balanced_accuracy_score
}
clfs = {
    "GNB": GaussianNB(),
    "KNN": KNeighborsClassifier(n_neighbors=1),
    "CART": DecisionTreeClassifier(random_state=1410)
}

ev = ws.evaluation.Evaluator(datasets=datasets,
                             protocol=(1, 5, 1410)).process(clfs=clfs)

scores = ev.score(metrics=metrics)
pt = ws.evaluation.PairedTests(ev)
tables = pt.process('t_test_13', corr=.1, std_fmt="(%.2f)")

for metric in tables:
    print("\n%s\n" % metric)
    print(tables[metric])

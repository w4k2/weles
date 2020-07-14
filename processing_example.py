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
import time

datasets = {
    "jeż": make_classification(random_state=1410, n_samples=1000),
    "kot": make_classification(random_state=1994, n_samples=1000),
    "lis": make_classification(random_state=1989, n_samples=1000),
    "byk": make_classification(random_state=1992, n_samples=1000,
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


start = time.time()
ev = ws.evaluation.Evaluator(datasets=datasets, store='storage',
                             protocol=(1, 5, 1410)).process(clfs=clfs)

end = time.time()
print("HELLO!")
print(end - start)

exit()
scores = ev.score(metrics=metrics)

# Kasia to właśnie ja
tables = ws.evaluation.PairedTests(ev).process(
    't_test_corrected', J=5, k=5, tablefmt="plain"
)

for metric in tables:
    print("\n%s\n" % metric)
    print(tables[metric])

# Smutna korekta
tables = ws.evaluation.PairedTests(ev).process(
    't_test_13', corr=.2, tablefmt="plain", std_fmt="(%.2f)"
)

for metric in tables:
    print("\n%s\n" % metric)
    print(tables[metric])

# I zwykły test
tables = ws.evaluation.PairedTests(ev).process(
    't_test_rel', corr=.2, tablefmt="github"
)

for metric in tables:
    print("\n%s\n" % metric)
    print(tables[metric])

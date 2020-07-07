"""
Class description

Date:
Authors:
"""

# imports
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.base import clone


class Evaluator():
    def __init__(self, datasets, protocol=(1, 5, None)):
        self.datasets = datasets
        self.protocol = protocol

    def process(self, clfs):
        """
        This function is used to process declared evaluation protocol
        through all given datasets and classifiers.
        It results with stored predictions and corresponding labels.

        Input atguments description:
        clfs: dictonary that contains estimators names and objects
              ["name"] : obj
        """
        self.clfs = clfs

        # Establish protocol
        m, k, random_state = self.protocol

        skf = RepeatedStratifiedKFold(n_splits=k, n_repeats=m,
                                      random_state=random_state)
        self.predictions = np.zeros([len(self.datasets), len(self.clfs),
                                     m*k])
        self.true_values = np.zeros([len(self.datasets), m*k])
        for dataset_id, dataset_name in self.datasets:
            X, y = self.datasets[dataset_name]
            for fold_id, (train, test) in enumerate(skf.split(X, y)):
                self.true_values[dataset_id, fold_id] = y[test]
                for clf_id, clf_name in self.clfs:
                    clf = clone(self.clfs[clf_name])
                    clf.fit(X[train], y[train])
                    y_pred = clf.predict(X[test])
                    self.predictions[dataset_id, clf_id, fold_id] = y_pred

        return self

    def score(self, metrics, return_std=True):
        """
        description

        Input arguments description:
        metrics: dictonary that contains metrics names and functions
                 ["name"] : function
        """
        _ = (len(self.datasets), len(self.clfs), len(metrics))

        self.scores = np.zeros(_)

        # Flatten or not...
        if return_std:
            self.stds = np.zeros(_)
            return self.scores, self.stds

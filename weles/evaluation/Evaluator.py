"""
Class description

Date:
Authors:
"""

# imports
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold


class Evaluator():
    def __init__(self, datasets, protocol=(1, 5, None)):
        self.datasets = datasets
        self.protocol = protocol

    def process(self, clfs):
        """
        description

        clfs: dictonary that contains estimators names and objects
              ["name"] : obj
        """
        self.clfs = clfs

        # Establish protocol
        m, k, random_state = self.protocol

        skf = RepeatedStratifiedKFold(n_splits=k, n_repeats=m,
                                      random_state=random_state)

        return self

    def score(self, metrics, return_std=True):
        """
        description

        metrics: dictonary that contains metrics names and functions
                 ["name"] : function
        """
        _ = (len(self.datasets), len(self.clfs), len(metrics))

        self.scores = np.zeros(_)

        # Flatten or not...
        if return_std:
            self.stds = np.zeros(_)
            return self.scores, self.stds

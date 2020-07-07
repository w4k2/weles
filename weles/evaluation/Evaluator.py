"""
Class description

Date:
Authors:
"""

# imports
import numpy as np


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
        return self

    def score(self, metrics, return_std=True):
        """
        description

        metrics: dictonary that contains metrics names and functions
                 ["name"] : function
        """
        self.metrics = metrics
        self.scores = np.zeros(((len(self.datasets),len(self.clfs), len(self.metrics)))

        if return_std:
            self.stds = np.zeros(((len(self.datasets), len(self.clfs), len(self.metrics)))
        return self.scores

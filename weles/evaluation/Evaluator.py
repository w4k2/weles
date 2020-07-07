"""
Class description

Date:
Authors:
"""

# imports


class Evaluator():
    def __init__(self, datasets, protocol):
        self.datasets = datasets
        self.protocol = protocol

    def process(self, clfs):
        """
        description

        clfs: dictonary that contains estimators names and objects
              ["name"] : obj
        """
        pass

    def score(self, metrcis):
        """
        description

        metrics: dictonary that contains metrics names and functions
                 ["name"] : function
        """
        pass

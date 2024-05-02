"""interface file to manage the general problem"""
from abc import ABC, abstractmethod

class IProblemSolver(ABC): #pylint: disable=R0903
    """class to set the problem structure"""
    @abstractmethod
    def compute_results(self, number) :
        """method to calculate the result of a number"""

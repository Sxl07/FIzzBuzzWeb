"""this file contains the code to calculate the fizzbuzz"""
from .i_problem_solver import IProblemSolver #pylint: disable=E0402

class FizzBuzz(IProblemSolver): #pylint: disable=R0903
    """class to define the 'problem' """
    def compute_results(self,number):
        """Method to compute the fizzbuzz value"""
        output = "Fizz" * (int(number) % 3 == 0) + "Buzz" * (int(number) % 5 == 0)
        return output or str(number)

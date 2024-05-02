"""App file to manage the methods (GET,POST,DELETE)"""
from data_storage.db_storage import DBStorage
from data_storage.i_data_storage import IDataStorage
from problem_solver.fizzbuzz import FizzBuzz
from problem_solver.i_problem_solver import IProblemSolver

class MyApp():
    """Class for the operation of DBStorage's methods"""
    def __init__(self) -> None:
        self.storage:IDataStorage = DBStorage()
        self.fizzbuzz:IProblemSolver = FizzBuzz()

    def get(self,number):
        """Method to work in general with GET"""
        result = self.storage.get_num(number)
        if result is None:
            return "Not Found",404
        return f'{result[0]} , {result[1]}',200

    def post(self,number):
        """Method to work in general with POST"""
        result_active = self.storage.get_active(number)
        result = self.storage.get_num(number)
        if result_active is None:
            if result is None:
                self.storage.insert_new_number([number,self.fizzbuzz.compute_results(number)])
                return f'{number},{self.fizzbuzz.compute_results(number)}',201 
            self.storage.activate_num(number)
            return f'{result[0]}, {result[1]}',200
        return f'{result[0]}, {result[1]}',409

    def delete(self,number):
        """Method to work in general with DELETE"""
        result=self.storage.get_active(number)
        if result is None:
            return "Not Found",404
        self.storage.deactivate_num(number)
        return "",204

    def range_post(self,min_limit,max_limit):
        """Method to work in general with POST(range)"""
        result = self.storage.get_range(min_limit,max_limit)
        if len(result)==0:
            return "Not Found",404
        outputrange=""
        for element in result:
            outputrange+= f'{element[0]},{element[1]}\n'
        return outputrange,200

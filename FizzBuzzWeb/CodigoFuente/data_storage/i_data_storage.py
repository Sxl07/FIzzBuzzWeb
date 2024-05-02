"""Interface file to manage the storage"""
from abc import ABC, abstractmethod

class IDataStorage(ABC):
    """Class to declare the methods for work in the database"""
    @abstractmethod
    def get_num(self,number):
        """method to request for a number"""
    @abstractmethod
    def get_active(self,number):
        """method to check if a number is active"""
    @abstractmethod
    def insert_new_number(self,number):
        """method to insert a new number"""
    @abstractmethod
    def activate_num(self,number):
        """method to activate a number"""
    @abstractmethod
    def deactivate_num(self,number):
        """method to deactivate a number"""
    @abstractmethod
    def get_range(self,min_limit,max_limit):
        """method to request for a range of numbers"""

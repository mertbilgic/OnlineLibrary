#https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
import pymongo
from helpers.config_helpers import get_value_from_name 

class MongoSingleton:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if MongoSingleton.__instance == None:
            MongoSingleton.__instance = pymongo.MongoClient(get_value_from_name('mongodb_client'))

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if MongoSingleton.__instance == None:
            MongoSingleton()
        return MongoSingleton.__instance
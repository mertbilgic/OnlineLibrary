import pymongo
from helpers.config_helpers import get_value_from_name 

class MongoSingleton:
    __instance = None

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if MongoSingleton.__instance == None:
            MongoSingleton()
        return MongoSingleton.__instance
        
    def __init__(self):
        """ Virtually private constructor. """
        if MongoSingleton.__instance == None:
            MongoSingleton.__instance = pymongo.MongoClient(get_value_from_name('mongodb_client'))

libraryClient = MongoSingleton.getInstance()

library_db = libraryClient[get_value_from_name('db_name')]

books_col = library_db[get_value_from_name('books_col')]

users_col = library_db[get_value_from_name('users_col')]



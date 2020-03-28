#https://mongodb.tecladocode.com/mongodb_with_python/database.py.html#code-for-database-py
from helpers.mongo_helpers import *

class Database:

    libraryClient = MongoSingleton.getInstance()

    library_db = libraryClient[get_value_from_name('db_name')]

    books_col = library_db[get_value_from_name('books_col')]

    users_col = library_db[get_value_from_name('users_col')]

    rent_col = library_db[get_value_from_name('rent_col')]
    
    @staticmethod
    def insert(collection, data):
        return Database.library_db[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.library_db[collection].find(query)
    
    @staticmethod
    def find_all(collection):
        return Database.library_db[collection].find()

    @staticmethod
    def find_one(collection, query):
        return Database.library_db[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.library_db[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.library_db[collection].remove(query)



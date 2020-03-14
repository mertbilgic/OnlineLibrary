import pymongo
from helpers.config_helpers import get_value_from_name 

libraryClient = pymongo.MongoClient(get_value_from_name('mongodb_client'))

library_db = libraryClient[get_value_from_name('db_name')]

books_col = library_db[get_value_from_name('books_col')]

users_col = library_db[get_value_from_name('users_col')]



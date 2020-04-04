#https://mongodb.tecladocode.com/mongodb_with_python/database.py.html#code-for-database-py
from helpers.mongo_helpers import *
from helpers.date_helpers import *

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

    @staticmethod
    def book_transfer(remove_col,insert_col,query,data):
        Database.remove(remove_col,query)
        Database.insert(insert_col,data)

    @staticmethod
    def insert_rent_col(remove_col,insert_col,query,id):
        book = Database.find_one(remove_col,query)
        rent_days = 7
        book.update({
                    "renter_user_id":id,
                    "deliver_date":Date.get_date_time(rent_days)
                    })
        Database.book_transfer(remove_col,insert_col,query,book)

    @staticmethod
    def deliver_book(remove_col,insert_col,query):
        book = Database.find_one(remove_col,query)
        if bool(book):
            del book['renter_user_id']
            del book['deliver_date']
            Database.book_transfer(remove_col,insert_col,query,book)
            return "İade işlemi başarılı","success"
        else:
            return "Belirtiğiniz kitap kullanıcıya ait değil.","danger"



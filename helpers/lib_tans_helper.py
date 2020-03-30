from helpers.db_crud import *

def rent_book(ISBN,id):
    now = datetime.today().strftime('%Y-%m-%d')
    rent_book = Database.find("RentBooks",{ "renter_user_id":id})
    message = "Kitap alma işlemini başarıyla gerçekleştirdiniz."
    result = "success"
    deliver_date = [x for x in rent_book if x['deliver_date'] < now]
    if rent_book.count()<3:
        if len(deliver_date)<=0:
                Database.insert_rent_col('Books','RentBooks',{"ISBN":ISBN},id)
        else:
            message = "Teslim tarihi geçmiş kitabınız bulunmaktadır."
            result = "danger"
    else:
        message = "Kitap kotanız dolmuştur."
        result = "danger"
    
    return message,result




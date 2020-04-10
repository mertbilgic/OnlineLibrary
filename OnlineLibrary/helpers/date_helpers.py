from datetime import datetime,timedelta

class Date:
 
    next_day = 0

    @staticmethod
    def get_date_time(days=0):
        date = (datetime.now()+timedelta(days=(Date.next_day+days))).strftime("%Y-%m-%d")
        return date
    @staticmethod
    def set_next_day(day):
        Date.next_day = day
    
import time
import datetime

def get_time():
    local_time = time.localtime()

    current_time = time.strftime("%H-%M-%S", local_time)
   

    return current_time
def get_date():
    date = datetime.date.today()
    today_is = date.strftime("%d-%m-%Y")
    return today_is

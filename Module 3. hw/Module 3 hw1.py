import datetime


date_string = "2020.10.09"
user_date =  datetime.datetime.strptime(date_string, "%Y.%m.%d")
user_date_only = user_date.date()
print(user_date_only)



def new_func():
    today_date = datetime.datetime.now()
    today_date_only = today_date.date()
    return today_date_only

today_date_only = new_func()
print(today_date_only)

 
get_days_from_today = today_date_only - user_date_only
print (get_days_from_today.days)








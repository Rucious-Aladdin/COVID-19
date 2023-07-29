import datetime
import os
date_lists = []
today = datetime.datetime.now()
today = today.strftime("%Y-%m-%d")

target_date = datetime.datetime(2019, 12, 31, 13, 35, 42, 657813)

while(1):
    target_date = target_date + datetime.timedelta(days=1)
    str_target_date = target_date.strftime("%Y-%m-%d")
    date_lists.append(str_target_date)
    if today == str_target_date:
        break

print(date_lists)
print(datapath)

#for index, date in enumerate(date_lists):
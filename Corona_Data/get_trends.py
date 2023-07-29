import pandas as pd
from pytrends.request import TrendReq
import time

code = {'Korea':'KR', 'USA':'US', 'France':'FR', 'Italia':'IT'}

kw_list = ['/m/0cjf0', '/m/0418s3', '/m/01b_21']

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

pytrends = TrendReq(hl='en-US', tz=360, requests_args={'headers':headers})

for name, c in code.items():
    l = list()
    for i, k in enumerate(kw_list):
        data = pytrends.get_historical_interest([k], year_start=2022, month_start=1, day_start=1, hour_start=0, year_end=2022, month_end=10, day_end=13, hour_end=0, cat=0, geo=c, sleep=60, frequency='daily')
        del data['isPartial']
        data.rename(columns={k:str(i) + k}, inplace=True)
        l.append(data)
        time.sleep(10)

    data = pd.concat(l, ignore_index=False, axis=1)
    data.to_csv("res_%s.csv" % name)
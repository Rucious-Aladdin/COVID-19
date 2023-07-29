import pandas as pd
import numpy as np
import datetime


def data_process(date, i):
    filename = "Covid_19"
    datapath1 = "/media/suseong/One Touch/CoronaData/CovidBackUp/"
    datapath = datapath1 + '%s_%s_%s.csv' % (filename, date.strftime("%Y_%m_%d"), 'korean')
    savepath = "/media/suseong/One Touch/CoronaData/model/"
    pre_data = pd.read_csv(datapath)
    pre_data["date"] = date.strftime("%Y-%m-%d")
    pre_data.dropna()
    pre_data.to_csv(savepath + date.strftime("%Y-%m-%d") + "_전처리.csv")

def concatdata():
    target_date = datetime.datetime(2020, 1, 3, 1, 35, 42, 657813)
    savepath = "/media/suseong/One Touch/CoronaData/model/"
    result = pd.read_csv(savepath + target_date.strftime("%Y-%m-%d") + "_전처리.csv")
    for i in range(2, 706):  # 1옆의 숫자를 변경해서 지정
        target_date = target_date + datetime.timedelta(days=1)
        df = pd.read_csv(savepath + target_date.strftime("%Y-%m-%d") + "_전처리.csv")
        result = pd.concat([result, df])

    result.to_csv(savepath + "final_concat.csv")

if __name__ == "__main__":
    target_date = datetime.datetime(2020, 1, 2, 1, 35, 42, 657813)
    for i in range(1, 706): # 1옆의 숫자를 변경해서 지정
        target_date = target_date + datetime.timedelta(days=1)
        data_process(target_date, i)

    concatdata()
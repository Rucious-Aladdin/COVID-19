from soykeyword.proportion import CorpusbasedKeywordExtractor
import pandas as pd
import datetime

def load_file(filename):
    save_path = "/media/suseong/One Touch/CoronaData/model/"
    df = pd.read_csv(save_path + filename)
    return df

def save_file(filename, savedata):
    save_path = "/media/suseong/One Touch/CoronaData/model/"
    savedata.to_csv(save_path + filename)

if __name__ == "__main__":
    filename = "revised_keyword_v1.0.csv"
    df = load_file(filename)

    corpusbased_extractor = CorpusbasedKeywordExtractor(
        min_tf=100,
        min_df=30,
        tokenize=lambda x: x.strip().split(),
        verbose=True
    )

    corpusbased_extractor.train(df['word'].tolist())

    grad_data = load_file("covid_19_korea_grad.csv")
    target_date = datetime.datetime(2020, 1, 2, 1, 35, 42, 657813)
    strdate = target_date.strftime("%Y-%m-%d")

    for i in range(1, 3):
        df["kor_grad_%d" % i] = 0
    idx = 0
    
    while strdate != "2021-08-05":
        target_date = target_date + datetime.timedelta(days=1)
        strdate = target_date.strftime("%Y-%m-%d")
        for i in range(1, 3):
            value = grad_data.at[idx, "kor_grad_%d" % i]
            df.loc[df["date"] == strdate, "kor_grad_%d" % i] = value
        idx += 1

    save_file("final_dataset_ver_1.2.csv", df)

    label_list = []
    for i in range(1, 3):
        label_list.append("kor_grad_%d" % i)

    keyword_data = {}
    for l in label_list:
        print(l)
        print(df[df[l] == 1]['word'].index)
        keywords = corpusbased_extractor.extract_from_docs(df[df[l] == 1]['word'].index)
        for k in keywords[:20]:
            print(k)
        keyword_data[l] = keywords

    key_df = pd.DataFrame.from_dict(keyword_data, orient='index')
    key_df = key_df.transpose()
    save_file("Proportion_based_keyword_data_v1.2.csv", key_df)
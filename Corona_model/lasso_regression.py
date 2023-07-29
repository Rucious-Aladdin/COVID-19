import pandas as pd
from soykeyword.lasso import LassoKeywordExtractor
from sklearn.feature_extraction.text import CountVectorizer

def load_file(filename):
    save_path = "/media/suseong/One Touch/CoronaData/model/"
    df = pd.read_csv(save_path + filename)
    return df

def save_file(filename, savedata):
    save_path = "/media/suseong/One Touch/CoronaData/model/"
    savedata.to_csv(save_path + filename)

class Corpus:
    def __init__(self, fname):
        self.fname = fname
        self.length = 0
    def __iter__(self):
        with open(self.fname, encoding="utf-8") as f:
            for doc in f:
                yield doc.strip()
    def __len__(self):
        if(self.length == 0):
            with open(self.fname, encoding="utf-8") as f:
                for n_doc, _ in enumerate(f):
                    continue
                self.length = (n_doc + 1)
        return self.length

def make_sparse_matrix(word_data):

    vectorizer = CountVectorizer(min_df=0.001)
    x = vectorizer.fit_transform(word_data)
    print(x.shape)
    word2index = vectorizer
    index2word = sorted(
        vectorizer.vocabulary_,
        key=lambda x:vectorizer.vocabulary_[x]
    )
    return x, word2index, index2word

if __name__ == "__main__":
    df = load_file("final_dataset_ver_1.2.csv")
    word_data = df['word'].tolist()

    x, word2index, index2word = make_sparse_matrix(word_data)

    lassobased_extractor = LassoKeywordExtractor(
        min_tf=20,
        min_df=10
    )
    lassobased_extractor.train(x, index2word)


    """
    testdocs = lassobased_extractor.get_document_index("코로나")
    keywords = lassobased_extractor.extract_from_docs(
        testdocs,
        min_num_of_keywords=30
    )
    print(type(testdocs))
    print(type(testdocs[10]))
    """
    label_list = []
    for i in range(1, 3):
        label_list.append("kor_grad_%d" % i)

    keyword_data = {}
    for l in label_list:
        print(l)
        documents = df[df[l] == 1]['word'].index.tolist()
        print(type(documents))
        print(type(documents[10]))
        keywords = lassobased_extractor.extract_from_docs(
            documents,
            min_num_of_keywords=30
        )
        for k in keywords[:20]:
            print(k)
        keyword_data[l] = keywords

    key_df = pd.DataFrame.from_dict(keyword_data, orient='index')
    key_df = key_df.transpose()
    save_file("lasso_regression_keyword_data.csv", key_df)
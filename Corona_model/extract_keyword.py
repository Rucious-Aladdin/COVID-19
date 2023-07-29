import pandas as pd
from soynlp.word import WordExtractor
from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import NewsNounExtractor
from soynlp.tokenizer import LTokenizer

import re

def loadfile(filename):
    savepath = "/media/suseong/One Touch/CoronaData/model/"
    df = pd.read_csv(savepath + filename)
    return df

def savefile(filename, df):
    savepath = "/media/suseong/One Touch/CoronaData/model/"
    df.to_csv(savepath + filename)

def clean_text(df):
    text = (df['title'] + ' ' + df['content'])
    text = re.sub('[^A-Za-z0-9가-힣]', ' ', text)
    return {'clean': text}

def extract_word(df):
    clean = ' '.join(regexTokenizer.tokenize(df['clean']))
    word = tokenizer.tokenize(clean, remove_r=True)
    return {'word': ' '.join(word)}



if __name__ == "__main__":
    filename = "final_concat.csv"
    df = loadfile(filename)
    df = df[["date", "title", "content"]].dropna()
    clean = df.apply(clean_text, axis=1, result_type='expand')
    print(clean.head())

    sentences = clean["clean"].tolist()

    word_extr = WordExtractor(
        min_frequency=100,
        min_cohesion_forward=0.05,
        min_right_branching_entropy=0.0
    )
    word_extr.train(sentences)
    words = word_extr.extract()
    cohesion_score = {word : score.cohesion_forward for word, score in words.items()}

    noun_extractor = NewsNounExtractor()
    nouns = noun_extractor.train_extract(sentences)  # list of str like
    noun_scores = {noun: score.score for noun, score in nouns.items()}
    combined_scores = {noun: score + cohesion_score.get(noun, 0)
                       for noun, score in noun_scores.items()}
    combined_scores.update(
        {subword: cohesion for subword, cohesion in cohesion_score.items()
         if not (subword in combined_scores)}
    )

    tokenizer = LTokenizer(scores=combined_scores)
    regexTokenizer = RegexTokenizer()

    word = clean.apply(extract_word, axis=1, result_type='expand')
    df = pd.concat([df, clean, word], axis=1, join='inner')
    """
    savefile("revised_keyword_v1.0.csv", df)
    """


import pandas as pd
from collections import Counter

corpus = ["o gato está dormindo", "o cachorro está latindo", "o gato está correndo"]

words = []

for sentence in corpus:
    tks = sentence.split()
    for i in range(len(tks) - 1):
        words.extend([tks[i], tks[i+1]])

df = pd.DataFrame(words, columns=["word", "next"])

bi_cnt = df.groupby(["word", "next"]).size().reset_index(name='count')

def predict_next_word(word):
    cand = bi_cnt[bi_cnt['word'] == word]
    
    if cand.empty:
        return "Nenhuma sugestão encontrada."
    else:
        sorted_cand = cand.sort_values(by='count', ascending=False)
        return sorted_cand.iloc[0]['next']
    
print(predict_next_word("o"))   
print(predict_next_word("gato"))
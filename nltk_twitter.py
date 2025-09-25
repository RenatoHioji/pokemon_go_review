import nltk

post = ""

palavras = nltk.word_tokenize(post)
palavras_diferentes = set(palavras)

print(palavras_diferentes)
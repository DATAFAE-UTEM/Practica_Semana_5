
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


with open('out_text.txt', 'r') as miarchivo:
    texto = miarchivo.read()

stop_words = set(stopwords.words('spanish'))
word_tokens = word_tokenize(texto)

# Aplicamos una funcion para encontrar elementos que no estén en puntuación

word_tokens = list(filter(lambda token: token not in string.punctuation, word_tokens))
filtro = []

for palabra in word_tokens:
    if palabra is not stopwords:
        filtro.append(palabra)

print(word_tokens)

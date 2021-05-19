from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from collections import Counter
from collections import OrderedDict


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "í"),
        ("ó", "o"),
        ("ú", "u")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
        return s


with open('out_text.txt', 'r') as miarchivo:
    archivo = miarchivo.read()
    texto = archivo.lower()

stop_words = set(stopwords.words('spanish'))
word_tokens = word_tokenize(texto)

# Aplicamos una funcion para encontrar elementos que no estén en puntuación
word_tokens = list(filter(lambda token: token not in string.punctuation, word_tokens))
filtro = []

# Ciclo para revisar las palabras que no están en las stopwords
for palabra in word_tokens:
    if palabra not in stop_words:
        filtro.append(palabra)

print(word_tokens)
print(type(filtro))

# Contabilizar top n° palabras tras stopwords
c = Counter(filtro)
print(c.most_common(50))

# Orden de las mas repetidas
y = OrderedDict(c.most_common())

with open('revision.txt', 'w') as f:
    for k, v in y.items():
        f.write(f'palabra:{k} n°:{v}\n')  # Crear nueva linea por elemento; formato lista

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string
from collections import Counter
from collections import OrderedDict


'''
Paso 1: Se abre el archivo de texto y se le genera una limpieza base;
transformación a minúsculas, eliminación de espacios en blanco, números, puntuación 
y elementos web.
'''

with open('out_text.txt', 'r') as miarchivo:
    archivo = miarchivo.read()
    # Se transforma el texto en minúscula
    nuevo_texto = archivo.lower()
    # Eliminación de páginas web (palabras que empiezan por "http")
    nuevo_texto = re.sub('http\S+', ' ', nuevo_texto)
    # Eliminación de signos de puntuación
    regex = '[\\n°\\n\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~\\”\\“]'
    nuevo_texto = re.sub(regex, ' ', nuevo_texto)
    # Eliminación de números
    nuevo_texto = re.sub("\d+", ' ', nuevo_texto)
    # Eliminación de espacios en blanco multiples
    nuevo_texto = re.sub("\\s+", ' ', nuevo_texto)
    print(len(nuevo_texto))

# Tokenizamos en Español
stop_words = set(stopwords.words('spanish'))
tokens = word_tokenize(nuevo_texto)
print(tokens)

# Aplicamos una funcion para encontrar elementos que no estén en puntuación
tokens_clean = list(filter(lambda token: token not in string.punctuation, tokens))
filtro = []

# Ciclo para revisar las palabras que no están en las stopwords
for palabra in tokens_clean:
    if palabra not in stop_words:
        filtro.append(palabra)

print(len(filtro))
print(filtro)

tagged = nltk.pos_tag(filtro)
print(tagged)

'''
Paso 2: Se pasa a contar las palabras mas repetidas, para luego buscar,
detalladamente, las veces que aparece la palabra en un contexto.
'''
# Contabilizar top n° palabras tras stopwords
c = Counter(filtro)
print(c.most_common(15))

# Orden de las mas repetidas
y = OrderedDict(c.most_common(50))

# Generación de documento con palabras y fracuencias ('out_text')
with open('revision.txt', 'w') as f:
    for k, v in y.items():
        f.write(f'palabra:{k} n°:{v}\n')  # Genera documento en formato lista

tagged_c = nltk.pos_tag(y)
print(tagged_c)

# Match de palabra con oración
text = nltk.Text(word_tokenize(nuevo_texto))
match = text.concordance('Fecha') # Se cambia la palabra

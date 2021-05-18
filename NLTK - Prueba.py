import nltk
from nltk.corpus import stopwords
from tqdm import tqdm
import time as ti


# Cambia los caracteres del UFT8 por letras normales:

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


with open('C:\\Users\\marti\\OneDrive\\Desktop\\Datas\\PDf - modelo test\\out_text.csv', enconding="ISO-8859-1", errors="ignore") as f:
    content = f.read()

    tokenize = nltk.word_tokenize(content)

    token_limpio = []
    # Se aplica tokenizado según lengua elegida

    guardar = True
    for i in tqdm(tokenize):
        for word in stopwords.words('spanish'):
            if (word.lower() == i.lower()):
                # Si existe, no se guarda
                guardar = False

            if (guardar):
                if (len(i) > 2):
                    # Se guardan las palabras no existentes en el stopword
                    token_limpio.append(normalize(i))
            guardar = True

print(token_limpio)

# Los adjetivos, sustentivos y verbos no están tokenizados.

# Tag separa los AT, NN, VB, JJ.

tag = nltk.pos_tag(token_limpio)
for i in tag:
    if i[1] == 'NN':
        print(i[1])

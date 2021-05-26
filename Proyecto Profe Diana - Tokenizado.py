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
Paso 1: Se abre el archivo de texto y transforma a minúscula
'''


with open('out_text.txt', 'r') as miarchivo:
    archivo = miarchivo.read()
    # Se transforma el texto en minúscula
    nuevo_texto = archivo.lower()
    print(nuevo_texto)
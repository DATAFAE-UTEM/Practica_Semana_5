#!/usr/bin/python
# -*- coding: UTF-8 -*-


import spacy
from spacy import displacy

nlp = spacy.load('out_text.txt')

text = nlp.read()

doc=nlp(text)


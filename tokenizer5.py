import sys
import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import re

f2 = open('C:/Users/alies/PycharmProjects/NLP/holmes-tok.txt', 'w')

text = []
with open('C:/Users/alies/PycharmProjects/NLP/holmes.txt', 'r') as f:
    for line in f:
        text.append(line.strip())

text = ' '.join(text)
sentences = sent_tokenize(text)
for sen in sentences:
    tokens = word_tokenize(sen)
    for tok in tokens:
        f2.write(f'{tok}\n')

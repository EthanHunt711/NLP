import sys
import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import re

f2 = open(sys.argv[2])

text = []
with open(sys.argv[1]) as f:
    for line in f:
        text.append(line.strip())

text = ' '.join(text)
sentences = sent_tokenize(text)
for sen in sentences:
    tokens = word_tokenize(sen)
    for tok in tokens:
        print(tok)
    print()

f2.close()
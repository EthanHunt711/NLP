import sys
import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import re

f2 = open(sys.argv[2], 'w')

text = []
with open(sys.argv[1]) as f1:
    for line in f1:
        text.append(line.strip())

text = ' '.join(text)
sentences = sent_tokenize(text)
for sen in sentences:
    tokens = word_tokenize(sen)
    f2.write(f"{' '.join(tokens)}\n")


f2.close()
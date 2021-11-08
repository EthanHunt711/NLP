import re, sys

f2 = open('C:/Users/alies/PycharmProjects/NLP/dev1-tok.txt', 'w')

with open('C:/Users/alies/PycharmProjects/NLP/dev1-raw.txt', 'r') as f1:
    for line in f1:
        for token in re.split("\s+", line.strip()):
            f2.write(f'{token}\n')

f2.close()

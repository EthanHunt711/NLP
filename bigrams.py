import sys

start = "<s>"
cxt = start
word = ""
freq = {}
bigrams = {}
eos = False

# Count bigrams
with open(sys.argv[1]) as f:
    for line in f:
        if line == "\n":
            word = "<e>"
            eos = True
        else:
            word = line.rstrip()
        if cxt not in bigrams:
            bigrams[cxt] = []
        if (cxt, word) not in freq:
            freq[(cxt, word)] = 0
            bigrams[cxt].append(word)
        freq[(cxt,word)] += 1
        cxt = word
        if eos:
            cxt = start
            eos = False

# Print bigram frequencies
total = 0
for c in sorted(bigrams.keys()):
    for w in sorted(bigrams[c]):
        total =+ int(freq[(c,w)])
        print(c + "\t" + w + "\t" + str(freq[(c,w)]))


print(f'1. There are {len(bigrams)} bigrams in the corpus and {total} bigram types.')

    
    

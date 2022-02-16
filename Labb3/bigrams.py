import sys

start = "<s>"
cxt = start
word = ""
freq = {}
bigrams = {}
eos = False
f2 = open(sys.argv[2], 'w')
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
        freq[(cxt, word)] += 1
        cxt = word
        if eos:
            cxt = start
            eos = False


# Counting the total occurances
def tot_oc(w1):
    total = 0
    for w2 in bigrams[w1]:
        total += freq[(w1, w2)]
    return total


# Print bigram frequencies
for c in sorted(bigrams.keys()):
    for w in sorted(bigrams[c]):
        f2.write(f"{c}  {w} {round(freq[(c,w)]/tot_oc(c), 6)}\n")


f2.close()



    
    

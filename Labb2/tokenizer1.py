import re, sys

f2 = open(sys.argv[2], 'w')

#regex_pattern = "([-,;:.!?%\$\"]|--|\d+\.\d+|\w+\-\w+|\d+|n\'\w|[A-Z]\.[A-Z]\.[A-Z]\.|[A-Z][a-z]+\.|[A-Z][a-z]+\.[A-Z]\.|\w+)"
regex_pattern = "((n*\'\w)|[A-Z][a-z]*\.[A-Z]*\.*[A-Z]*\.*|\w*-+\w*|\$*\d+\.*\d+\%*|[-,;:.!?\"]|\w+)"
with open(sys.argv[1]) as f1:
    for line in f1:
        for token in re.findall(regex_pattern, line.strip()):
            if token == '"':
                token = "''"
            if token == ".":
                token = ".\n"
            f2.write(f'{token[0]}\n')

f2.close()

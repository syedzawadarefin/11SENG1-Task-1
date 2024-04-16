# memory puzzle - have to remember the order of the 3
# spelling bee 
# word meanings (spacy en-core-web-sm module)

import random

words = open("words.txt", 'r')
wordo = []
for c in words:
    wordo.append(c)

print(wordo[random.randint(0, len(wordo))])

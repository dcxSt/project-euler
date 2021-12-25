import numpy as np

# trinum = [n*(n+1)/2 for n in range(1,100)]

def word_to_score(word):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0
    for letter in word:
        score += 1 + alph.index(letter)
    return score

f = open("p042_words.txt","r")
lines = f.read()
f.close()
l = lines.split(",")
l = [w[1:-1] for w in l]

num_tri = 0
for word in l:
    score = word_to_score(word)
    if int(np.sqrt(2*score)) * int(np.sqrt(2*score) + 1) / 2 == score:
        num_tri += 1

print(num_tri)


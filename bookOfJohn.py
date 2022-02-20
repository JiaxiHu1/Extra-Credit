import csv 

infile = open('book of John text.csv','r')

readfile = infile.read()

per_word = readfile.split()

countFather = 0 
countGod = 0 
countChrist = 0 
countSpirit = 0 
countspirit = 0 
countlife = 0 
countman = 0 

for i in per_word: 
    if i == "Father":
        countFather += 1 
print("Father:",countFather)


for x in per_word: 
    if x == "God":
        countGod += 1 

print("God:",countGod)

for y in per_word: 
    if y == "Christ":
        countChrist += 1 

print("Christ:",countChrist)

for Z in per_word: 
    if Z == "Spirit":
        countSpirit += 1 

print("Spirit:",countSpirit)

for a in per_word: 
    if a == "spirit":
        countspirit += 1 

print("spirit:",countspirit)

for b in per_word: 
    if b == "life":
        countlife += 1 

print("life:",countlife)

for c in per_word: 
    if c == "man":
        countman += 1 

print("man:",countman)




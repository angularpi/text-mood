# -*- coding: utf-8 -*-
import csv
import numpy as np

#load words and score from dictionary.csv to arrays
words = []
score = []
with open ("dictionary.csv","rb") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        words.append(row[0])
        score.append(row[1])
#load input text from input.txt and clean it before procesing
f = open("input.txt", "r").read()
f = f.lower()
f = f.replace("'"," ")
f = f.replace('"',' ')
f = f.replace(',',' ')
f = f.replace('.',' ')
f = f.replace(';',' ')
f = f.replace(':',' ')
f = f.replace('?',' ')
f = f.replace('-',' ')
f = f.replace('!',' ')
f = f.replace('(',' ')
f = f.replace(')',' ')
f = f.split()
f = sorted(f)
print("length input: " + str(len(f)))

#main
output = []
frequency = []
rating = []
k=0
for w in f:
    if w not in output and w in words:
        output.append(w)
        count = float(f.count(w))
        frequency.append(f.count(w))
        rate = float(score[words.index(w)])
        rating.append(count*rate)      
        'print("Word: " + w + ", count: " + str(f.count(w)) + ", score: " + str(count*rate))'
        k += 1  
    else:
        pass
#print results    
print("length unique: " + str(len(output)))
print("Total: " + str(np.sum(rating)/np.sum(frequency)))

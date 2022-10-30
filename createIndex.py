import os
import csv
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import math

makeLemma = WordNetLemmatizer()
readPath = 'taggedFiles/'
entries = os.listdir(readPath)

# load pages
allPages = []
pagesId = {}
counter = 0;

for i in entries:
    path = readPath + i
    pagesId[counter] = i;
    counter += 1

    with open(path, 'r', encoding='utf-8') as f:
        words = list(csv.reader(f, delimiter='\t'))

    allPages.append(np.array(words))

# compute tf and tf-idf
pageId = 0
tfMatrix = {}
allWords = {}
idfMatrix = {}

for page in allPages:
    countOfWords = {}
    totalWords = len(page)

    for element in page:
        word = makeLemma.lemmatize(element[0])

        if word in countOfWords:
            countOfWords[word] += 1
        else:
            countOfWords[word] = 1

    for word in countOfWords:
        countOfWords[word] = countOfWords[word] / totalWords

        if word in allWords:
            allWords[word] += 1
        else:
            allWords[word] = 1

    tfMatrix[pageId] = countOfWords
    pageId += 1

for word in allWords:
    idfMatrix[word] = math.log10(len(allPages) / allWords[word])


tf_idf = []

for page in tfMatrix:
    metric = {}
    for word in tfMatrix[page]:
        metric[word] = tfMatrix[page][word] * idfMatrix[word]

    tf_idf.append(metric)

# save index in xml format
name = 'invertedIndex.xml'
with open(name, 'w', encoding='utf-8') as xmlFile:
    xmlFile.write('<inverted_index>\n')

    for lemma in allWords:
        xmlFile.write('<lemma name='+'"'+lemma+'"'+'>\n')
        for page in tfMatrix:
            if lemma in tfMatrix[page]:
                xmlFile.write('\t<document id= "' + str(pagesId[page]) + '"' + ' weight= "' + str(tf_idf[page][lemma]) + '"' + '/>\n')

        xmlFile.write('</lemma>\n')

    xmlFile.write('</inverted_index>')





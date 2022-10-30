import xml.etree.ElementTree as elTree
import time
import random
from operator import itemgetter
import numpy as np

invertedIndex = 'invertedIndex.xml'

tree = elTree.parse(invertedIndex)
allLemmas = tree.findall("./lemma")

indexDictionary = {}
wordsForQueries = []

i = 0
for lemma in allLemmas:
    name = lemma.get('name')
    documents = lemma.findall("./document")

    randNum = random.randint(1, 100)
    if i <= 300 and randNum < 10:
        wordsForQueries.append(name)
        i += 1

    # iterate trough all the document tags for every lemma
    for doc in documents:
        docId = doc.get('id')
        w = doc.get('weight')
        tup = [str(docId), float(w)]

        if name in indexDictionary:
            indexDictionary[name].append(tup)
        else:
            indexDictionary[name] = [tup]

totalTime = 0;
startTime = time.time()

for i in range(20):
    r = random.randint(1, 300)
    query = wordsForQueries[r]

    results = indexDictionary[query]
    results = np.array(sorted(results, key=itemgetter(1), reverse=True))

    endTime = time.time()
    totalTime = endTime - startTime

    print('Results for: ', query)
    print(results[:, 0])


# queries with 2 words
startTime = time.time()
for i in range(20):
    r = random.randint(1, 300)
    query1 = wordsForQueries[r]
    results1 = np.array(indexDictionary[query1])

    r = random.randint(1, 300)
    query2 = wordsForQueries[r]
    results2 = np.array(indexDictionary[query2])

    # find the common ids in the results of the two queries
    commonId = np.intersect1d(results1[:, 0], results2[:, 0], assume_unique=True)

    resultsTwo = []
    for i in commonId:
        # find the position of the common ids in every results array
        pos1 = np.where(results1[:, 0] == i)[0][0]
        pos2 = np.where(results2[:, 0] == i)[0][0]

        w = results1[pos1, 1] + results2[pos2, 1]
        tup = [i, w]
        resultsTwo.append(tup)

    endTime = time.time()
    totalTime = endTime - startTime

    if not resultsTwo:
        print('No documents for this query: ', query1, query2)
    else:
        resultsTwo = np.array(sorted(resultsTwo, key=itemgetter(1), reverse=True))
        print('Results for: ', query1, query2)
        print(resultsTwo[:, 0])


# queries with 3 words
startTime = time.time()
for i in range(1, 30):
    r = random.randint(1, 300)
    query1 = wordsForQueries[r]
    results1 = np.array(indexDictionary[query1])

    r = random.randint(1, 300)
    query2 = wordsForQueries[r]
    results2 = np.array(indexDictionary[query2])

    r = random.randint(1, 300)
    query3 = wordsForQueries[r]
    results3 = np.array(indexDictionary[query3])

    # find the common ids in the results of the three queries
    intersection = np.intersect1d(results1[:, 0], results2[:, 0], assume_unique=True)
    commonId = np.intersect1d(intersection, results3[:, 0], assume_unique=True)

    results = []
    for i in commonId:
        # find the position of the common ids in every results array
        pos1 = np.where(results1[:, 0] == i)[0][0]
        pos2 = np.where(results2[:, 0] == i)[0][0]
        pos3 = np.where(results3[:, 0] == i)[0][0]

        w = results1[pos1, 1] + results2[pos2, 1] + results3[pos3, 1]
        tup = [i, w]
        results.append(tup)

    endTime = time.time()
    totalTime = endTime - startTime

    if not results:
        print('No documents for this query: ', query1, query2, query3)
    else:
        results = np.array(sorted(results, key=itemgetter(1), reverse=True))
        print('Results for: ', query1, query2, query3)
        print(results[:, 0])


# queries with 4 words
startTime = time.time()
for i in range(1, 30):
    r = random.randint(1, 300)
    query1 = wordsForQueries[r]
    results1 = np.array(indexDictionary[query1])

    r = random.randint(1, 300)
    query2 = wordsForQueries[r]
    results2 = np.array(indexDictionary[query2])

    r = random.randint(1, 300)
    query3 = wordsForQueries[r]
    results3 = np.array(indexDictionary[query3])

    r = random.randint(1, 300)
    query4 = wordsForQueries[r]
    results4 = np.array(indexDictionary[query4])

    # find the common ids in the results of the four queries
    intersection1 = np.intersect1d(results1[:, 0], results2[:, 0], assume_unique=True)
    intersection2 = np.intersect1d(results3[:, 0], results4[:, 0], assume_unique=True)
    commonId = np.intersect1d(intersection1, intersection2, assume_unique=True)

    results = []
    for i in commonId:
        # find the position of the common ids in every results array
        pos1 = np.where(results1[:, 0] == i)[0][0]
        pos2 = np.where(results2[:, 0] == i)[0][0]
        pos3 = np.where(results3[:, 0] == i)[0][0]
        pos4 = np.where(results4[:, 0] == i)[0][0]

        w = results1[pos1, 1] + results2[pos2, 1] + results3[pos3, 1] + results4[pos4, 1]
        tup = [i, w]
        results.append(tup)

    endTime = time.time()
    totalTime = endTime - startTime

    if not results:
        print('No documents for this query: ', query1, query2, query3, query4)
    else:
        results = np.array(sorted(results, key=itemgetter(1), reverse=True))
        print('Results for: ', query1, query2, query3, query4)
        print(results[:, 0])


print('Average Response time:')
print(totalTime)






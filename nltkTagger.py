import os
import nltk

closedClassCategories = ['CD', 'CC', 'DT', 'EX', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP',
                         ' PRP$', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB', '', ':', '.', ',']

readPath = 'textFiles/'
writePath = 'taggedFiles/'

entries = os.listdir(readPath)
filedId = 0

for i in entries:
    path = readPath + i

    with open(path, 'r', encoding='utf-8') as f:
        fileToTokenize = f.read()

    fileToTokenize = nltk.word_tokenize(fileToTokenize)
    tags = nltk.pos_tag(fileToTokenize)

    tagFile = writePath + i.replace('.html', '', 2)
    with open(tagFile, 'w', encoding='utf-8') as f:
        for t in tags:
            if t[1] not in closedClassCategories:
                f.write(t[0] + '\t' + t[1] + '\n')

    filedId = filedId + 1

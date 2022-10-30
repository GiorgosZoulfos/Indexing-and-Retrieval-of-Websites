import os
from bs4 import BeautifulSoup

readPath = 'htmlPages/'
writePath = 'textFiles/'

entries = os.listdir(readPath)

for i in entries:
    path = readPath + i

    with open(path, 'rb') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

    onlyText = soup.get_text()
    textName = writePath + i

    with open(textName, 'w', encoding='utf-8') as f:
        f.write(onlyText)


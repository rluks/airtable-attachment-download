import csv
import re
import urllib.request
import unicodedata

filename = 'People-Raw.csv'

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

#with open(filename, 'r', encoding="mbcs") as csvfile:
with open(filename, 'r', encoding="utf-8") as csvfile:
    datareader = csv.reader(csvfile)
    count = 0
    for row in datareader:
        if(count == 0):
            count += 1
            continue
        name = row[0]
        urlrow = row[1]
        if(name == "" or urlrow == ""):
            continue
        urlbrackets = re.search("\(https:\/\/dl.airtable.com/.*\)$", urlrow)
        urlbracket = urlbrackets.group()[1:]
        url = urlbracket[:-1]
        nameascii2 = strip_accents(name)
        print(nameascii2)


        #urllib.request.urlretrieve(url, file_name)

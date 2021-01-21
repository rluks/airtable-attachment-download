import csv
import re
import urllib.request
import unicodedata
import html
from urllib.parse import urlparse
import os

filename = 'People-Raw.csv'

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def grab():
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

            nameascii = strip_accents(name)
            nameesc = html.escape(nameascii)

            path = urlparse(url).path
            ext = os.path.splitext(path)[1]
            
            file_name = nameesc + ext

            print("Grabbing " + file_name)
            urllib.request.urlretrieve(url, file_name)

grab()

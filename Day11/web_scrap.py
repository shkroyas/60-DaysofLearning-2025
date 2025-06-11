import nltk
import urllib
import bs4 as bs
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

#Data Source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming')

#Parsing the data/creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')

#Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

#Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

#Preparing the data
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

with open("tokenized_sentences.txt", "w", encoding="utf-8") as f:
    for sentence in sentences:
        f.write(" ".join(sentence) + "\n")








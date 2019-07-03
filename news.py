import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://www.hurriyet.com.tr/kelebek/saglik/gunes-carpmasi-nasil-gecer-gunes-carpmasina-ne-iyi-gelir-41262863'

response = requests.get(url) #Connect to url
print(response) #if response==200 OK

soup = BeautifulSoup(response.text,'html.parser') #create parser

#this query finds all paragraphes in news
paragraphe= soup.findAll('div',{'class' :'rhd-all-article-detail'})
print(paragraphe[0])


"""
for labelizing operations look url
http://www.hurriyet.com.tr/kelebek/<category:saglik>
when we store that news we have to create data for our model
"""

"""
Data Format :
Id word0 word1 word2 word3 word4 word5 ... category<label>
0  freq0 freq1 freq2 freq3 freq4 freq5 ... Saglik
1  freq0 freq1 freq2 freq3 freq4 freq5 ... Spor
...

Words and their frequency
"""

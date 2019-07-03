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
for labeling operations look url
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
class News():
    def __init__(self,category,content):
        self.__category = category
        self.__content = content
    
    def getCategory(self):
        return self.__category
    def getContent(self):
        return self.__content





#We have to find news url's
def find_news_url(response):
    #find news url here then parse all news and get their content, category
    soup = BeautifulSoup(response.text,'html.parser')

    news_url = soup.findAll('a') #finds all a tags.  But we need news

    #news_url[any_number]['href'] different usage

    return news_url
    

def _find_news(url,category):
    _url = url +'/'+category
    _response = requests.get(url)
    if _response == 200:
        pass
    #Fetch news belong to that <category>

    #prepare soup
    _soup = BeautifulSoup(_response.text,'html.parser')

    _news = soup.findAll('a') #find all <category> news and return them

    return _news[:]['href']


def _newsContent(url,category):
    #find news content according to url and return News object
    _response  = requests.get(url)
    if _response == 200:
        pass # do stuff here
    
    _soup = BeautifulSoup(_response.text,'html.parser')
    dirty_content = _soup.findAll('p',{'class':'rhd-all-article-detail'}) #its dirty content for us

    #cleaning stuff here...
    _content = dirty_content # cleaned version

    #This query has to change for hurriyet i guess this query like that
    return News(category,_content)

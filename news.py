import requests
import urllib.request
import time
from bs4 import BeautifulSoup

"""url = 'http://www.hurriyet.com.tr/kelebek/saglik/gunes-carpmasi-nasil-gecer-gunes-carpmasina-ne-iyi-gelir-41262863'

response = requests.get(url) #Connect to url
print(response) #if response==200 OK

soup = BeautifulSoup(response.text,'html.parser') #create parser

#this query finds all paragraphes in news
paragraphe= soup.findAll('div',{'class' :'rhd-all-article-detail'})
print(paragraphe[0])
"""

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

    def __str__(self):
        return 'Title : {0} \nContent : {1}'.format(self.__category,self.__content)




    

def _findNews(url,category):
    _url = url +'/'+category
    _response = requests.get(url)
    if _response == 200:
        pass
    #Fetch news belong to that <category>

    #prepare soup
    _soup = BeautifulSoup(_response.text,'html.parser')

    #this query using for finding news links.
    _news = _soup.findAll('a',{'class':'main-news-box'}) #find all <category> news and return them


    #This query using for finding titles of news. 
    #_news = _soup.findAll('h3',{'class':'box-title'})
    return _news


def _newsContent(url,category):
    #find news content according to url and return News object
    _response  = requests.get(url)
    if _response == 200:
        pass # do stuff here
    
    _soup = BeautifulSoup(_response.text,'html.parser')
    dirty_content = _soup.findAll('div',{'class':'rhd-all-article-detail'}) #its dirty content for us

    #cleaning stuff here...
    _content = dirty_content # cleaned version

    #This query has to change for hurriyet i guess this query like that
    return News(category,_content)



__category = 'ekonomi'
"""
All economy news titles. on the main page.
news_list = _findNews('http://www.hurriyet.com.tr/ekonomi/',__category)
for i in news_list:
    try:
        print(i['title'])
    except:
        print('Author ')
"""


"""

This base function finds news_url's

news_list = _findNews('http://www.hurriyet.com.tr/ekonomi',__category)
for i in news_list:
    try:
        print(i['href'])
    except:
        print('Unknown')


__url = 'http://www.hurriyet.com.tr'+news_list[0]['href']
print(__url)
a_news =_newsContent(__url,__category)
print(a_news)
"""

#Sample usage : 
#First find news_url's then for every url find news contents. 

list_of_news = []

news_list = _findNews('http://www.hurriyet.com.tr/ekonomi',__category)
for i in news_list:
    try:
        __url = 'http://www.hurriyet.com.tr'+i['href']
        list_of_news.append(_newsContent(__url,__category)) #it is still dirty content 
        time.sleep(1) #sleep every time while fetching the website
        #for not marking as a spammer.

    except:
        print('Unknown news')

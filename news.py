import requests
from bs4 import BeautifulSoup
import sys
import time
import news_parser as parser
import pandas


class News():
    def __init__(self,category,title,content):
        self.__category = category
        self.__title = title
        self.__content = content

    def getCategory(self):
        return self.__category
    def getTitle(self):
        return self.__title
    def getContent(self):
        return self.__content
    def __str__(self):
        return "Category<{0}>\nTitle<{1}>\nContent<{2}>".format(self.__category,self.__title,self.__content)

__url = "https://tr.sputniknews.com/"+sys.argv[1]+"/"
parser.start_connection(url =__url )
news_link = None
#if news size parameter entered.
if len(sys.argv)>2:
    news_link = parser.get_links(int(sys.argv[2]))
else:
    news_link = parser.get_links()

parser.close_connection()

def clean(dirty_content):
    return dirty_content.text #return clean content

def _news_content(url):
    #get response from url 
    _response = requests.get(url) # if 200 ok.

    _soup = BeautifulSoup(_response.text,'html.parser') #create html parser
    _dirty_content = _soup.find('div',{'class':'b-article__text'}) #get dirty_content

    _clean_content = clean(_dirty_content)

    #we need to get title too.
    return News(sys.argv[1],'title',_clean_content)


def __news_objects(news_link):
    news = []
    print("Searching......")
    for i in news_link:
        #time.sleep(0.5)
        news.append(_news_content(i))

    return news

def _clear_content(content):
    #© this sign exists
    _dirty = str(content)
    _dirty = _dirty.replace('©','')
    _dirty = _dirty.replace('\n','')
    return _dirty




news_objects = __news_objects(news_link)
news_data = [[]]
for i in news_objects:
    news_data.append([i.getCategory(),i.getTitle(),_clear_content(i.getContent())])

news_dataframe = pandas.DataFrame(news_data)
print('Data Frame Version' )
print(news_dataframe)

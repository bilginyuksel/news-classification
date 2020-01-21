import requests
from bs4 import BeautifulSoup
import sys
import time
import news_parser as parser
import pandas
import prepare_news as pn
import terms


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

# __url = "https://tr.sputniknews.com/"+sys.argv[1]+"/"
# parser.start_connection(url =__url )
# news_link = None
# #if news size parameter entered.
# if len(sys.argv)>2:
#     news_link = parser.get_links(int(sys.argv[2]))
# else:
#     news_link = parser.get_links()

# parser.close_connection()

def clean(dirty_content):
    return dirty_content.text #return clean content

def _news_content(url,category):
    #get response from url 
    _response = requests.get(url) # if 200 ok.

    _soup = BeautifulSoup(_response.text,'html.parser') #create html parser
    _dirty_content = _soup.find('div',{'class':'b-article__text'}) #get dirty_content

    _clean_content = clean(_dirty_content)

    #we need to get title too.
    return News(category,'title',_clean_content)


def __news_objects(news_link,category):
    news = []
    print("Searching......")
    for i in news_link:
        #time.sleep(0.5)
        news.append(_news_content(i,category))

    return news

# def _clear_content(content):
#     #© this sign exists
#     _dirty = str(content)
#     _dirty = _dirty.replace('©','')
#     _dirty = _dirty.replace('\n','')
#     return _dirty




# news_objects = __news_objects(news_link,sys.argv[1])
# news_data = [[]]
# last_news = None
# for i in news_objects:
#     news_data.append([i.getCategory(),i.getTitle(),_clear_content(i.getContent())])
#     last_news = _clear_content(i.getContent())



"""
NOTE !!!!
this code block written for only test purposes on the real usage
you can't use this code because, values are not lists here and cout variable 
initalizes to 0 for once. If you solve this issues you can use this code.
"""

news_terms = terms.getTermsList() #Our dataframes columns
data = {}
#initialize dictionarys columns
# for i in news_terms:
#     data[i] =[0 for i in range(60)] 

#dataframe key,value
#data['key'] = value..  // data['key'] = [values...]

#after initialization of data columns now fill one row with one news
#means you will calculate the frequency of each terms
# for i in range(len(news_objects)):
#     cout = 0
#     news = pn.conjuction_prepositions(pn.listModel(pn.clear(news_objects[i].getContent())))
#     for j in news:
#         for k in news_terms:
#             if k in j:
#                 cout +=1 #cout storing for % 
#                 data[k][i]+=1


# #this loops for finding repeating percents. %
# summ = 0
# for i in news_terms:
#     for j in range(len(news_objects)):
#         summ += data[i][j]
#     for j in range(len(news_objects)):
#         if summ!=0:
#             data[i][j] /= summ
#     summ = 0 

def help_clean(data):
    return pn.conjuction_prepositions(pn.listModel(pn.clear(data)))


def getMultipleNews(category):
    global news_terms
    global data
    # get so much link
    __url = "https://tr.sputniknews.com/"+"ekonomi"+"/"
    parser.start_connection(url =__url)
    links = parser.get_links()
    parser.close_connection()
    __url = "https://tr.sputniknews.com/"+"spor"+"/"
    parser.start_connection(url =__url)
    links += parser.get_links()
    parser.close_connection()
    __url = "https://tr.sputniknews.com/"+"politika"+"/"
    parser.start_connection(url =__url)
    links += parser.get_links()
    parser.close_connection()
    __url = "https://tr.sputniknews.com/"+"yasam"+"/"
    parser.start_connection(url =__url)
    links += parser.get_links()
    parser.close_connection()
    __url = "https://tr.sputniknews.com/"+"dunya"+"/"
    parser.start_connection(url =__url)
    links += parser.get_links()
    parser.close_connection()

    for i in news_terms:
        data[i] =[0 for i in range(len(links))] 

    news = __news_objects(links,category)
    for i in range(len(news)):
        cout = 0
        __news = pn.conjuction_prepositions(pn.listModel(pn.clear(news[i].getContent())))
        for j in __news:
            for k in news_terms:
                if k in j:
                    cout +=1 #cout storing for % 
                    data[k][i]+=1

    #this loops for finding repeating percents. %
    summ = 0
    for i in news_terms:
        for j in range(len(news)):
            summ += data[i][j]
        for j in range(len(news)):
            if summ!=0:
                data[i][j] /= summ
        summ = 0 


"""
this method should work for calculating % data[i] /= cout 
not working on this version i didn't debug it .

#calculate the percent of repeating number
for i in news_terms:
    try:
        data[i] /= cout
    except:
        #for zero division error
        pass
"""

getMultipleNews('ekonomi')
# getMultipleNews('spor')
# getMultipleNews('politika')
# getMultipleNews('saglik')

print(data) #Sample data output.
dataFrame = pandas.DataFrame(data)
print(dataFrame)
dataFrame.to_csv('data.csv',index=False)

#print dataFrame


# list_of_words = []
# for i in news_objects:
#     list_of_words = list_of_words+pn.conjuction_prepositions(pn.listModel(pn.clear(i.getContent())))
#     print(pn.conjuction_prepositions(pn.listModel(pn.clear(i.getContent())))) #what i want
    


# model = pn.frequency(pn.create_model(pn.final_cleaning(list_of_words)))

# model.to_csv("output.csv")



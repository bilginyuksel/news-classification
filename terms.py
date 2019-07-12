from bs4 import BeautifulSoup
import requests


def routineSoupPreparation(url):
    #Routine things
    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')
    return soup
    


class Terms():
    #Scraping terms need's to clear. Not fits the news style.
    __terms = ""
    def economy(self):
        soup = routineSoupPreparation('https://www.uyumsoft.com/bilmeniz-gereken-temel-ekonomi-terimleri/')
        terms = soup.find('div',{'class':'avia_textblock av_inherit_color'}).find_all('strong')
        self.__terms += " " + str(terms)
    def politics(self):
        soup = routineSoupPreparation('https://www.on5yirmi5.com/haber/guncel/politika/462/siyasi-terimler-sozlugu.html')
        terms = soup.find('div',{'class':'article-content article-body-responsive col-lg-9'}).find_all('strong')
        self.__terms += " " + str(terms)
    def world(self):
        #find better website for scraping...
        soup = routineSoupPreparation('https://www.dunyaatlasi.com/cografya-terimleri-sozlugu/')
        terms = soup.find('div',{'id':'searchContent'}).find_all('strong')
        self.__terms += " " + str(terms)
    def sport(self):
        soup = routineSoupPreparation('https://www.dersimiz.com/terimler-sozlugu/Futbol-Terimleri-Sozlugu-70-Sayfa-2.html')
        terms = soup.find('article').find_all('strong')
        self.__terms += " " + str(terms)
    def health(self):
        soup = routineSoupPreparation('https://blog.konusarakogren.com/ingilizce-tibbi-terimler/')
        
        terms = soup.find('div',{'class','post-inner'}).find_all('p')
        self.__terms += " " + str(terms)
    
    def terms(self):
        return self.__terms.lower()

    def collectTerms(self):
        self.economy()
        self.politics()
        #self.world()
        self.sport()
        self.health()

def getTermsList():
    """
    get all terms as a string data type. 
    and clear all of the useless_tags from this terms string
    after clearization return list of these terms.
    """
    t = Terms()
    t.collectTerms()
    _terms = t.terms() #terms are set and sets are not iterable
    useless_tags = ['strong','<br/>','<br>','<p','p>','\r','\n','>','<','/','!','[',']',':',',','\xa0']
        
    for i in useless_tags:
        _terms =_terms.replace(i,' ')
    
    return list(set(_terms.split()))

from bs4 import BeautifulSoup
import requests


def routineSoupPreparation(url):
    #Routine things
    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')
    return soup
    


class Terms():
    #Scraping terms need's to clear. Not fits the news style.
    __terms = []
    def economy(self):
        soup = routineSoupPreparation('https://www.uyumsoft.com/bilmeniz-gereken-temel-ekonomi-terimleri/')
        terms = soup.find('div',{'class':'avia_textblock av_inherit_color'}).find_all('strong')
        for i in terms:
            self.__terms.append(str(i))
    def politics(self):
        soup = routineSoupPreparation('https://www.on5yirmi5.com/haber/guncel/politika/462/siyasi-terimler-sozlugu.html')
        terms = soup.find('div',{'class':'article-content article-body-responsive col-lg-9'}).find_all('strong')
        for i in terms:
            self.__terms.append(str(i))
    def world(self):
        #find better website for scraping...
        soup = routineSoupPreparation('https://www.dunyaatlasi.com/cografya-terimleri-sozlugu/')
        terms = soup.find('div',{'id':'searchContent'}).find_all('strong')
        for i in terms:
            self.__terms.append(str(i))
    def sport(self):
        soup = routineSoupPreparation('https://www.dersimiz.com/terimler-sozlugu/Futbol-Terimleri-Sozlugu-70-Sayfa-2.html')
        terms = soup.find('article').find_all('strong')
        for i in terms:
            self.__terms.append(str(i))
    def health(self):
        soup = routineSoupPreparation('https://blog.konusarakogren.com/ingilizce-tibbi-terimler/')
        # new usage of terms . should be like that .
        # terms = str(soup.find('div',{'class','post-inner'}).find_all('p'))
        # useless_tags = ['strong','>','<','/','[',']',':',',','\xa0']
        # terms.lower()
        # for i in useless_tags:
        #     terms.replace(i,' ')
        # terms = terms.split()

        for i in terms:
            self.__terms.append(str(i))
    def terms(self):
        return set(self.__terms)

    def getAllTerms(self):
        self.economy()
        self.politics()
        #self.world()
        self.sport()
        self.health()

def getTermsList():
    t = Terms()
    t.getAllTerms()
    all_terms = list(t.terms()) #terms are set and sets are not iterable

    #clean tags from terms recent using tags are stored below.
    tags = ['strong', '<p', 'p>', ',', ':', '/','br','\r','\n','\xa0','<','>']

    for i in range(len(all_terms)):
        all_terms[i] = all_terms[i].lower()
        for j in tags:
            all_terms[i] = all_terms[i].replace(j,'')
    while '' in all_terms:
        all_terms.remove('')

    return all_terms

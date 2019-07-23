from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

driver = None

def start_connection(driver_path="geckodriver.exe",url = 'https://tr.sputniknews.com/'):
    #__url = url +sys.argv[1]+'/' #https://tr.sputniknews.com/ekonomi/
    global driver
    driver = webdriver.Firefox(executable_path = driver_path)
    driver.get(url)



def get_links(click_time = 1):
    #time.sleep(1)
    print('Searching....')

    for i in range(click_time):
        time.sleep(1.2)
        driver.find_element_by_css_selector('.b-btn.m-more').click()



    selen = driver.find_elements_by_css_selector('.b-stories__img')
    print('News length :',len(selen))
    links = []
    for i in selen:
        links.append(i.get_attribute('href'))


    return links

def close_connection():
    driver.close()




from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('C:/Users/91916/Downloads/chromedriver_win32')
browser.get(START_URL)

def scrape():
    headers = ['Name','Distance','Mass','Radius']
    planet_list = []

    for i in range(0,501):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class','exoplanet'}):
            li_tags = ul_tag.find_all('li')
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
            planet_list.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[1]')
        with open('scrappar_2.csv','w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(planet_list)
scrape()
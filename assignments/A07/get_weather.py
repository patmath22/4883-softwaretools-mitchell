"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time                                             # needed for the sleep function

from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager
from rich import print
import gui
import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        #service = Service(executable_path='/usr/local/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(options=options)  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 3 seconds for dynamic data to load...")
        time.sleep(3)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit() 
        with open('table1.html','w') as f:
              f.write(driver.page_source)                                                     # quit ChromeDriver
        return render                                               # return the page source HTML
    
if __name__=='__main__':

    # Could be a good idea to use the buildWeatherURL function from gui.py
    #url = 'http://www.wunderground.com/history/daily/KCHO/date/2020-12-31'
    url = gui.buildWeatherURL()


    # get the page source HTML from the URL
    #page = asyncGetWeather(url)

    with open('table2.html',encoding='utf-8') as f:
       page=  f.read()
    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    
    # find the appropriate tag that contains the weather data
    tables = soup.find_all('table')
    #print(tables[1].text)

    #tables = soup.find_all('table')
    
    
     
    
    # with open('table1.html') as f:
    #      table = f.read()
    #      soup = BeautifulSoup(table, 'html.parser')
    
    
    
# print(soup.prettify())
# print(soup.text)
    allData = []
    keys=[]

    head = tables[1].find_all('th')
    rows = tables[1].find_all('tr')


    for d in head:
         key = d.text.strip().replace(' ','').replace('\n','')
         keys.append(key)
    
    for row in rows: 
        row = row.find_all('td')
        data = []
        for td in row:
            # print(data.text.strip().replace(' ','').replace('\n',''))
            # print("====================================")
            data.append(td.text.strip().replace(' ','').replace('\n','').replace('\xa0',''))

        dictionary = dict(zip(keys, data))
        allData.append(dictionary)

print(allData)
stuff =[]        

for row in allData:
     if len(row)>0:
          stuff.append(row)

print("-----------------"*5)

print(stuff[0].keys())  #returns column headers

for row in stuff:
    #  print(row['Time'])
    for k,v in row.items():
         print(k,v)     #to access value only print(v)


    # print the parsed HTML
    #print(history.prettify())
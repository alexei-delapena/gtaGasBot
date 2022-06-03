import re
from bs4 import BeautifulSoup
from selenium import webdriver

CLEANR = re.compile('<.*?>')

def cleanRegex(string):
    cleantext = re.sub(CLEANR, '', string)
    return cleantext

chromepath = r"C:\Users\Alexei\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromepath)
url = "https://toronto.citynews.ca/toronto-gta-gas-prices/"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
results = soup.find('div', attrs={'class' : 'float-box'})
msg = results.findAll('p').text

print(msg)


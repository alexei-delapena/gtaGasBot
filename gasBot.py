import discord
from bs4 import BeautifulSoup
from selenium import webdriver
from os import system

TOKEN = 'OTc5NjExNTc0NzgyMjc1NTg0.GaNyi6.MsHlPFPBPjThZGXW4W2rBtp6YC8cczpyb7mEag'

client = discord.Client()

chromepath = r"C:\Users\Alexei\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromepath)

def gasChangeTomorrow():
    url = "https://toronto.citynews.ca/toronto-gta-gas-prices/"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find('div', attrs={'class' : 'float-box'}).text
    return results

def gasByCity(city):
    chromepath = r"C:\Users\Alexei\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromepath)
    url = "https://www.gasbuddy.com/gasprices/ontario/"
    cityURL = url + city + "/"
    driver.get(cityURL)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    station_elements = soup.find_all('div', attrs={'class' : 'GenericStationListItem-module__stationListItem___3Jmn4'})

    for station_element in station_elements:
        name = station_element.find('h3', attrs={'class' : 'header__header3___1b1oq header__header___1zII0 header__midnight___1tdCQ header__snug___lRSNK StationDisplay-module__stationNameHeader___1A2q8'}).text
        address = station_element.find('div', attrs={'class' : 'StationDisplay-module__address___2_c7v'})
        for br in address('br'):
            br.replace_with('\n')
        price = station_element.find('span', attrs={'class' : 'text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL'}).text
        print(name)
        print(address.text)
        print(price + '\n')

text = gasChangeTomorrow()

@client.event
async def on_ready():
    print("Gas Bot online!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("gas"):
        await message.channel.send(text)

    else:
        await message.channel.send("Invalid call. Type gas to get the next gas price.")


try:
    client.run(TOKEN)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system('kill 1')

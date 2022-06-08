import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from selenium import webdriver


class gasBotCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def on_ready(self):
        print("Gas Bot online!")

    @commands.command()
    async def leave(self, ctx):
        await ctx.channel.disconnect()

    @commands.command()
    async def tomorrow(self, ctx):
        text = gasChangeTomorrow()
        await ctx.channel.send(text)

    @commands.command()
    async def city(self, ctx, *searchstring):
        info = gasByCity(tupleToString(*searchstring))
        await ctx.channel.send(info)

def tupleToString(*tuple):
    delimiter = '-'
    string = str(delimiter.join(tuple))
    return string

def gasChangeTomorrow():
    chromepath = r"C:\Users\Alexei\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromepath)
    url = "https://toronto.citynews.ca/toronto-gta-gas-prices/"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find('div', attrs={'class' : 'float-box'}).text
    return results

def gasByCity(city):
    text = ''
    chromepath = r"C:\Users\Alexei\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromepath)
    url = "https://www.gasbuddy.com/gasprices/ontario/"
    cityurl = url + city + "/"
    driver.get(cityurl)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    station_elements = soup.find_all('div', attrs={'class' : 'GenericStationListItem-module__stationListItem___3Jmn4'})

    for station_element in station_elements:
        name = station_element.find('h3', attrs={'class' : 'header__header3___1b1oq header__header___1zII0 header__midnight___1tdCQ header__snug___lRSNK StationDisplay-module__stationNameHeader___1A2q8'}).text
        address = station_element.find('div', attrs={'class' : 'StationDisplay-module__address___2_c7v'})
        for br in address('br'):
            br.replace_with('\n')
        price = station_element.find('span', attrs={'class' : 'text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL'}).text
        text = text + str(name) + '\n' + str(address.text) + '\n' + str(price) + '\n\n'

    return text

def setup(client):
    client.add_cog(gasBotCommands(client))
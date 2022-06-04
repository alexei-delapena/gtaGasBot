import discord
from bs4 import BeautifulSoup
from selenium import webdriver
from os import system

TOKEN = 'OTc5NjExNTc0NzgyMjc1NTg0.G5FP5S.OCTm86ktVcYxb8fBz7JTgYtlRJDk0RJmL4jOlA'

client = discord.Client()


def gasChangeTomorrow():
    chromepath = r"C:\Users\Alexei\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromepath)
    url = "https://toronto.citynews.ca/toronto-gta-gas-prices/"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find('div', attrs={'class' : 'float-box'}).text
    return results


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

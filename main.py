import discord
from discord.ext import commands
import gasBotCommands

cogs = [gasBotCommands]

client = commands.Bot(command_prefix ='gas ', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTc5NjExNTc0NzgyMjc1NTg0.G3hnkP.Cylv2lTH2N1w6e2kXv6j3h4-xU4N-hBHdMENrM")
from email import message
from inspect import getcomments
import os
import random
from time import sleep
import time
import requests, re
import discord
from discord.ext import commands

TOKEN = (open("env/TOKEN_KEY", "r")).read()

# for HTML tag cleaner
CLEANR = re.compile('<.*?>') 

# threads data
threads_data = []
# for comments data
comments_data = []

# Discord bot values

# DISCORD BOT
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

# BOT commands
@bot.command()
async def test(ctx):
    print("test passed")
    pass

# BOT events
@bot.event
async def on_ready():
    print(f'{bot.user.name} has joined Discord!')

# Если добавлены какие либо реакции
@bot.event
async def on_reaction_add(reaction, user):
    
    # игнорируем бота
    if user == bot.user:
        return
    
@bot.event
async def on_message(message):
    
    print(f'time: {time.strftime("%H:%M:%S")}, {message.author} : {message.content}')
    
    # игнорируем сообщения бота
    if message.author == bot.user:
        return
    
    # ADD REACTION if Role id=1016367823490134027 name='гильдия хуёв
    # Если чебурек из гильдии хуев добавляем эмоци какашки
    if str(message.author.roles).find('1016367823490134027') != -1:
            await message.add_reaction('💩')
        
    await bot.process_commands (message)

bot.run(TOKEN)
# client.run(TOKEN)
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import os
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='a!')

@bot.event
async def on_ready():
    print('Bot is ready!')
    await bot.change_presence(game=discord.Game(name="a!"))

@bot.command(pass_context=True)
async def online(ctx):
    await bot.say(" bot is **online** :green_heart: ")

bot.run(os.getenv(BOT_TOKEN)

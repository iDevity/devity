import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import requests
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


@bot.command(pass_context=True)
async def pingwildin(ctx):
    await bot.say(" @dev_wildin#3121 ")

@bot.command(pass_context=True)
async def mag8ball(ctx):
    await bot.say(random.choice(["It is decidedly so :8ball:",
                                   "Without a doubt :8ball:",
                                   "Yes, definitely :8ball:",
                                   "You may rely on it :8ball:",
                                   "As I see it, yes :8ball:",
                                   "Most likely :8ball:",
                                   "Outlook good :8ball:",
                                   "Yes :8ball:",
                                   "Signs point to yes :8ball:",
                                   "Reply hazy try again :8ball:",
                                   "Ask again later :8ball:",
                                   "Better not tell you now :8ball:",
                                   "Cannot predict now :8ball:",
                                   "Concentrate and ask again :8ball:",
                                   "Don't count on it :8ball:",
                                   "My reply is no :8ball:",
                                   "My sources say no :8ball:",
                                   "Outlook not so good :8ball:",
                                   "Very doubtful :8ball:"]))



bot.run(process.env.BOT_TOKEN)

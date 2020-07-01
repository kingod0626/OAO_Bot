import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('NzI3Njk5NTI1NTMxMzM2NzA1.XvwBIQ.1YPIke5_a-xsN9Pj4jfq01FgXNk')
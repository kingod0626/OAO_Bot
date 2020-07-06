import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f"{member} leave!")
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        for msgkey in (jdata['msgkeywords']):
            if msgkey in msg.content and msg.author != self.bot.user:
                await msg.channel.send('你好啊旅行者')



def setup(bot):
    bot.add_cog(Event(bot))
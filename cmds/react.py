import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 婆(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)#<--如果是網路上的圖片不須轉換資料
        await ctx.send(file=pic)

    @commands.command()
    async def 我婆占卜(self, ctx):
        random_pic = random.choice(jdata['net_pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def 指令(self, ctx):
        await ctx.send(jdata['func'])

    @commands.command()
    async def 說(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command()
    async def 酒神(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(React(bot))
import discord
from discord.ext import commands
from discord.ext.commands.core import command
import aiohttp
from asyncdagpi import Client, ImageFeatures
import io
from io import BytesIO

class Image(commands.Cog):
  def __init__(self, client
  ):
    self.client = client
  @commands.command()
  async def dog(self, ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/dog')
        factjson = await request2.json()

        embed = discord.Embed(title="Doggo!", color=discord.Color.purple())
        embed.set_image(url=dogjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)

  @commands.command()
  async def cat(self, ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/cat')
        catjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/cat')
        factjson = await request2.json()
        embed = discord.Embed(title="Cat eh?!", color=discord.Color.purple())
        embed.set_image(url=catjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)

  
  @commands.command()
  async def birb(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/birb')
          birbjson = await request.json()
          # This time we'll get the fact request as well!
          request2 = await session.get('https://some-random-api.ml/facts/birb')
          factjson = await request2.json()

          embed = discord.Embed(title="Birb!", color=discord.Color.purple())
          embed.set_image(url=birbjson['link'])
          embed.set_footer(text=factjson['fact'])
          await ctx.send(embed=embed)

  @commands.command()
  async def panda(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/panda')
          pandajson = await request.json()
          # This time we'll get the fact request as well!
          request2 = await session.get('https://some-random-api.ml/facts/panda')
          factjson = await request2.json()
          embed = discord.Embed(title="Panda ig?!", color=discord.Color.purple())
          embed.set_image(url=pandajson['link'])
          embed.set_footer(text=factjson['fact'])
          await ctx.send(embed=embed)


  @commands.command()
  async def koala(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/koala')
          koalajson = await request.json()
          # This time we'll get the fact request as well!
          request2 = await session.get('https://some-random-api.ml/facts/koala')
          factjson = await request2.json()
          embed = discord.Embed(title="Koala ig?!", color=discord.Color.purple())
          embed.set_image(url=koalajson['link'])
          embed.set_footer(text=factjson['fact'])
          await ctx.send(embed=embed)

  @commands.command(pass_context=True)
  async def meme(self,ctx):
      embed = discord.Embed(title = "Memes")
      
      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://meme-api.herokuapp.com/gimme/memes') as r:
              res = await r.json()
              embed.set_image(url=res['url'])
              await ctx.send(embed=embed)
  @commands.command()
  async def sketch(self, ctx, *, member: discord.Member = None):
      '''Sketches the avatar'''
      if not member:
          member = ctx.author
      url = member.avatar.url
      async with ctx.typing():
          img = BytesIO(await url.read())
          img.seek(0)
          buffer = await self.sketch(img)
      await ctx.send(file=discord.File(buffer, filename="sketch.png"))

  @commands.command()
  async def triggered(self, ctx, member: discord.Member=None):
      if not member: # if no member is mentioned
          member = ctx.author # the user who ran the command will be the member
          
      async with aiohttp.ClientSession() as trigSession:
          async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar.url}') as trigImg: # get users avatar as png with 1024 size
              imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
              
              await trigSession.close() # closing the session and;
              
              await ctx.reply(file=discord.File(imageData, 'triggered.gif'))
  @commands.command()
  async def trigger(self, ctx, member:discord.Member = None):
    urlig = f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar.url}"
    embed = discord.Embed(
      title = f"{member} is TRIGGERED :triggered1::triggered2:",
      description = " ",
      colour = discord.Color.yellow()
      )
    
    await ctx.send(urlig) 
def setup(bot):
  bot.add_cog(Image(bot))

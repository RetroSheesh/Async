import discord
from discord.ext import commands
from discord.ext.commands.core import command
from variable import randomanimelist
import random
import animec
import requests

class Anime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def randomanime(self, ctx):
      member: discord.Member
      embed69 = discord.Embed(title=("RANDOM ANIME"),
                              description=(random.choice(randomanimelist)),
                              colour=discord.Color.blue())
      await ctx.send(embed=embed69)
      if ctx.guild == None:
          await ctx.send("No DMS PLEASE")

  @commands.command()
  async def animequote(self, ctx):
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animu/quote")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json.sentence() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    await ctx.send(content)

  @commands.command()
  async def anime(self, ctx, *, query):
    try:
        anime = animec.Anime(query)
    except:
        await ctx.send(embed= discord.Embed(description = "No corresponding Anime is found for the search query",color = discord.Color.blue()))
        return
    embed = discord.Embed(title = anime.title_english,url = anime.url,description = f"{anime.description[:200]}...",color = discord.Color.random())
    embed.add_field(name = "Episodes",value = str(anime.episodes))
    embed.add_field(name = "Rating",value = str(anime.rating))
    embed.add_field(name = "Broadcast",value = str(anime.broadcast))
    embed.add_field(name = "type",value = str(anime.type))
    embed.add_field(name = "NSFW status",value = str(anime.is_nsfw()))
    await ctx.send(embed = embed)
    

def setup(bot):
  bot.add_cog(Anime(bot))

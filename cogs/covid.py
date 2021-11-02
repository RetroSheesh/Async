import discord
from discord.ext import commands
import random
import asyncio
import requests

class Covid(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def covid(self, ctx, *, countryName = None):
    url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
    stats = requests.get(url)
    json_stats = stats.json()
    country = json_stats["country"]
    totalCases = json_stats["cases"]

    totalDeaths = json_stats["deaths"]

    recovered = json_stats["recovered"]
    active = json_stats["active"]
    critical = json_stats["critical"]
    casesPerOneMillion = json_stats["casesPerOneMillion"]
    deathsPerOneMillion = json_stats["deathsPerOneMillion"]
    totalTests = json_stats["totalTests"]

    embed2 = discord.Embed(
      title=f"**COVID-19 Status  for {country}**!", 
      description="This information is not 100% accurate", 
      colour=0xff0000, 
      timestamp=ctx.message.created_at)
    embed2.add_field(name="**Total Covid casess**", value=totalCases, inline=True)
    embed2.add_field(name="**Total Covid deaths**", value=totalDeaths, inline=True)
    embed2.add_field(name="**Recovered people**", value=recovered, inline=True)
    embed2.add_field(name="**Active Covid cases**", value=active, inline=True)
    embed2.add_field(name="**Covid critical patients**", value=critical, inline=True)
    embed2.add_field(name="**Cases per 1 million**", value=casesPerOneMillion, inline=True)
    embed2.add_field(name="**Deaths per 1 million**", value=deathsPerOneMillion, inline=True)
    embed2.add_field(name="**Total tests**", value=totalTests)
    
    await ctx.send(embed=embed2)



def setup(bot):
  bot.add_cog(Covid(bot))


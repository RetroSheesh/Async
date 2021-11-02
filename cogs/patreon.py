import discord
from discord.ext import commands
import random
import asyncio

class Patreon(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def patreon(ctx):
      embed = discord.Embed(title=("Patreon for Async"),
                            description=(""),
                            colour=discord.Color.blue())
      embed.add_field(
          name="Support us!",
          value=
          "Async bot is a free to play bot and is available to everyone for free, however you can support us and get a lot of discord server perks and bot perks."
      )
      embed.add_field(
          name="Patreon link",
          value="You can support us [here](https://www.patreon.com/join/asyncbot)"
      )

      await ctx.send(embed=embed)
  @commands.command()
  async def supportuswhen(self, ctx):
    class MyView(discord.ui.View):
        @discord.ui.button(label="Important invite links",
                           style=discord.ButtonStyle.primary)
        async def button_callback(self, button, interaction):
            button.disabled = True
            button.label = 'No more pressing!'
            await interaction.response.edit_message(view=self)

    view = discord.ui.View()
    view.add_item(
        discord.ui.Button(
            label='Invite the bot ',
            url=
            'https://discord.com/api/oauth2/authorize?client_id=880645664915210312&permissions=2147483680&scope=bot',
            style=discord.ButtonStyle.url))
    view.add_item(
        discord.ui.Button(
            label='Invite the bot (Admin)',
            url=
            'https://discord.com/api/oauth2/authorize?client_id=880645664915210312&permissions=8&scope=bot',
            style=discord.ButtonStyle.url))
    view.add_item(
        discord.ui.Button(label='Support Server',
                          url='https://discord.gg/8eR3Mkyknv',
                          style=discord.ButtonStyle.url))
    embed = discord.Embed(
      title = f"Support us!",
      description = " ",
      colour = discord.Color.gold()
    )
    embed.add_field(name = "We are a F2P bot! ", value = "Async is a bot which is 100% free to bot and do not restrict anything behind a paywall, but we still do need some money to keep the bot running and pay for the hosting.")
    embed.add_field(name = "How can you support us?", value = "You can either buy ")
    await ctx.send('Press the button!', view=view)

def setup(bot):
  bot.add_cog(Patreon(bot))

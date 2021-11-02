import discord
from discord.ext import commands
import random
import asyncio
from afks import afks
import datetime, time
from discord import Spotify

class utility(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def dm(ctx, member: discord.Member, *, content: str):
      try:
          await member.send(content)
          await ctx.send(f"Direct message Sent successfully to {member.mention} "
                        )
      except:
          await ctx.member.send("Member has their DMS closed")


  @dm.error
  async def zoomba(ctx, error):
      if isinstance(error, discord.ext.commands.MissingRequiredArgument):
          embed = discord.Embed(title=(
              "User or Messages is a required argument which is missing!!"),
                                description=("Format: `-dm {user} {messages} `"),
                                colour=discord.Color.blue())
          await ctx.send(embed=embed)
  @commands.command()
  async def membercount(ctx):
    members = ctx.guild.member_count
    embed345 = discord.Embed(
        title=("Member count"),
        description=
        (f"<:arrow_884975740947406950:884975759045849128> Members : {members} "
         ),
        colour=discord.Color.red())
    embed345.set_footer(
        text="Keep going! You will reach a lot of members one day <3")
    await ctx.send(embed=embed345)
  @commands.command()
  async def afk(self, ctx, *, reason ="No reason provided"):
      member = ctx.author
      if member.id in afks.keys():
          afks.pop(member.id)
      else:
          try:
              await member.edit(nick = f"(AFK) {member.display_name}")
          except:
              pass
      afks[member.id] = reason
      embed = discord.Embed(title = ":zzz: Member AFK", description = f"{member.mention} has gone AFK",color = member.color)
      embed.set_author(name=self.client.user.name)
      embed.add_field(name='AFK note: ',value=reason)
      await ctx.send(embed=embed)
  @commands.command()
  async def poll(self, ctx, *, question: str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=(f"{ctx.author.name} asks"),
                          description=(f"{question}"),
                          colour=discord.Color.blue())
    my_msg = await ctx.send(embed=embed)
    await my_msg.add_reaction("<:TickYes:887310159678959637>")
    await my_msg.add_reaction("<:TickNeutral:887312614101762098>")
    await my_msg.add_reaction("<:RedTick:887310266499469322>")

  esnipes = {}

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
        guild = before.guild
        channel = before.channel
        guildEditedMsgs = self.esnipes.get(guild.id, {})
        channelEditedMsgs = guildEditedMsgs.get(channel.id, [])
        
        if len(channelEditedMsgs) >= 5:
            channelEditedMsgs = channelEditedMsgs[-5:]
        channelEditedMsgs.append({'before' : before, 'after' : after})
        guildEditedMsgs[channel.id] = channelEditedMsgs
        self.esnipes[guild.id] = guildEditedMsgs
    
  @commands.command(aliases = ['esn'])
  async def esnipe(self, ctx):
        gsn = self.esnipes.get(ctx.guild.id, {})
        if gsn:
            csn = gsn.get(ctx.channel.id, [])
            if csn:
                msg = csn[-1]
                bf, af = msg['before'], msg['after']
                embed = discord.Embed(description = f'**channel:** {ctx.channel.mention}\n\n**Original Message:**\n{bf.content}\n\n**Edited Message:**\n{af.content}\n\n[Jump to the message]({bf.jump_url})')
                embed.set_author(name = bf.author.name, icon_url = bf.author.avatar.url)
                embed.set_footer(text = f'Esnipe Request: {ctx.author.name}', icon_url = ctx.author.avatar.url)
                await ctx.send(embed=embed)
            else:
                await ctx.send('`There\'s nothing to snipe here!`')
        else:
            await ctx.send('`There\'s nothing to snipe here!`')

  @commands.command()
  async def emojis(self, ctx):
    emoji_count = len(ctx.guild.emojis)
    await ctx.send(f"{emoji_count}")

  @commands.command()
  async def uptime(self, ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(
      title = f"Uptime of {discord.client.user}",
      description = uptime,
      colour = discord.Color.blurple()
      )
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(utility(bot))

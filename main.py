import discord
import random
from random import choice
from discord.ext import commands, tasks
from keep_alive import keep_alive
import os
import aiohttp
import io
import asyncio
from discord.ext.commands import CommandNotFound, has_permissions, MissingPermissions
import sqlite3
import textwrap
import urllib
import datetime
import re
from discord import Spotify

# def get_prefix(client, message):
#     conn = sqlite3.connect("prefix.db")
#     c = conn.cursor()
#     with conn:
#         c.execute("""SELECT * FROM prefix_data WHERE guild_id = :id""",
#                   {"id": message.guild.id})
#         data = c.fetchone()
#         return data[1]


client = commands.Bot(command_prefix=["a.", "a!"])
client.start_time = 0.0

# conn = sqlite3.connect("prefix.db")
# c = conn.cursor()
# try:
#     with conn:
#         c.execute("""CREATE TABLE prefix_data (
#         guild_id integer,
#         prefix string
#         )""")
#         print("Created table")
# except:
#     print("Prefix database already exists terminated creation job!")

statuses = [
"to a!help", "My development", "75+ COMMANDS"
]


# @client.event
# async def on_guild_join(guild):
#     conn = sqlite3.connect("prefix.db")
#     c = conn.cursor()
#     with conn:
#         c.execute("""INSERT INTO prefix_data VALUES (:guild_id, :prefix)""", {
#             "guild_id": guild.id,
#             "prefix": "."
#         })


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(
        name=random.choice(statuses)))


@client.event
async def on_ready():
    print(f"{client.user} is now ready!")
    print("Bots online \n Remember to load all the cogs lmfaooo")
    for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
        try:
          client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
          print(f"{e.__class__.__name__}: {e}")
    await change_status.start()


@client.command()
async def load(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename}")
            except Exception as e:
                print(f"{e.__class__.__name__}: {e}")
    await ctx.send("Loaded all cogs")





# @client.command()
# @commands.has_permissions(administrator=True)
# async def prefix(ctx: commands.Context, *, prefix: str):
#     try:
#         prefix = str(prefix)
#         conn = sqlite3.connect("prefix.db")
#         c = conn.cursor()
#         with conn:
#             c.execute(
#                 """UPDATE prefix_data SET prefix = :prefix WHERE guild_id = :id""",
#                 {
#                     "prefix": prefix,
#                     "id": ctx.guild.id
#                 })
#             await ctx.send(f"Successfully changed prefix to {prefix}")

#     except discord.ext.commands.errors.MissingPermissions:
#         await ctx.send("Missing permissions!")


@client.command()
async def support(ctx):
    embed3 = discord.Embed(
        title="Bot support server link",
        description=
        "To  the join the bot support server, [click here](https://discord.gg/bQ6D6XM9SA)",
        colour=discord.Color.blue())
    embed3.set_footer(text="Join the server when?-")
    embed3.set_thumbnail(url=ctx.author.avatar.url)
    embed3.set_author(name=client.user)
    await ctx.send(embed=embed3)

@client.command()
async def ping(ctx):
    latencyclient = round((client.latency * 1000))
    message = await ctx.send("Ping Pong 🏓")
    await message.edit(content=f"My ping is **{latencyclient}m/s** ")


# @client.event
# async def on_message(message):
#     if message.content.startswith('<@!880645664915210312>'):
#         conn = sqlite3.connect("prefix.db")
#         c = conn.cursor()
#         with conn:
#             c.execute("""SELECT * FROM prefix_data WHERE guild_id = :id""",
#                       {"id": message.guild.id})
#             data = c.fetchone()
#         await message.channel.send(
#             f'The prefix of the bot in the server is `{data[1]}`\n Run `{data[1]}help` to get the commands list'
#         )
#     await client.process_commands(message)


@commands.Cog.listener()
async def on_dbl_vote(self, data):
    user = data['user']
    embed = discord.Embed(description="New Vote! Voter: {}".format(user))
    channel = self.client.get_channel(int(889737442163294259))
    await channel.send(embed=embed)

@client.command()
async def icon(ctx):
    icon_url = ctx.guild.icon.url

    embed = discord.Embed(title=(f"{ctx.guild.name}'s icon"),
                          description=(""),
                          colour=discord.Color.gold())

    embed.set_image(url=(icon_url))
    await ctx.send(embed=embed)


@client.command(aliases=['ytcomment', 'youtubecomment'])
async def comment(ctx, member: discord.Member = None, *, comment: str):
    avatar = member.avatar.replace(format='png', size=1024)
    name = member.name
    embed = discord.Embed(
      colour = 0xffff99
    )
    embed.set_image(
        url=
        f'https://some-random-api.ml/canvas/youtube-comment?&avatar={avatar}&comment={comment}&username={name}'
    )
    await ctx.send(embed=embed)


snipe_message_author = {}
snipe_message_content = {}


@client.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]


@client.command()
async def custombot(ctx):
    embed = discord.Embed(
        title=("CUSTOM BOT HELP "),
        description=
        ("You can ask for help regarding custom bot [here](https://discord.gg/bQ6D6XM9SA)"
         ))
    await ctx.send(embed=embed)







@client.command()
async def wcrules(ctx):
    embed = discord.Embed(title=("WC RULES"),
                          description=("""Maps-

Summit
Standoff
Raid
Take-Off
Firing Range
Hackney Yard
Meltdown

Rules-

Guns
NA-45

Operator Skills
H.I.V.E
Shadow Blade
Transform Shield
Bull Charge
Ballistic Shield

Lethal Utility
Trip Mine
Thermite
Molotov Cocktail

Tactical Utility
Heartbeat Sensor
Gas Grenades

Perks
Persistence
Restock

Weapon Perks
Akimbo

Scorestreaks
UAV
Shock RC
Advanced UAV
Counter UAV
Care Package
Shield Turret
Stealth Chopper
Hawk X3
VTOL
All Emotes are restricted from use during any point of a match"""))
    await ctx.send(embed=embed)


@client.command()
async def fetch_commands(ctx):
    if ctx.author.name == "Retro":
        for command in client.commands:
            await ctx.send(command)
    else:
        await ctx.send("Dev only command!!")


@client.command(
    aliases=['l', 'song', 'lyric']
)  # adding aliases to the command so they they can be triggered with other names
async def lyrics(ctx, *, search=None):
    """A command to find lyrics easily!"""
    if not search:  # if user hasnt given an argument, throw a error and come out of the command
        embed = discord.Embed(
            title="No search argument!",
            description="You havent entered anything, so i couldnt find lyrics!"
        )
        return await ctx.reply(embed=embed)

    song = urllib.parse.quote(
        search
    )  # url-encode the song provided so it can be passed on to the API
    message = await ctx.send("Searching song...", delete_after=3)
    await message.edit(content="Searching for lyrics...")
    await message.edit(content="Seaching for artist...")
    async with aiohttp.ClientSession() as lyricsSession:
        async with lyricsSession.get(
                f'https://some-random-api.ml/lyrics?title={song}'
        ) as jsondata:  # define jsondata and fetch from API
            if not 300 > jsondata.status >= 200:  # if an unexpected HTTP status code is recieved from the website, throw an error and come out of the command
                return await ctx.send(
                    f'Recieved poor status code of {jsondata.status}')

            lyricsData = await jsondata.json(
            )  # load the json data into its json form

    error = lyricsData.get('error')
    if error:  # checking if there is an error recieved by the API, and if there is then throwing an error message and returning out of the command
        return await ctx.send(f'Recieved unexpected error: {error}')

    songLyrics = lyricsData['lyrics']  # the lyrics
    songArtist = lyricsData['author']  # the author's name
    songTitle = lyricsData['title']  # the song's title
    songThumbnail = lyricsData['thumbnail'][
        'genius']  # the song's picture/thumbnail

    for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace=False):
        embed = discord.Embed(title=songTitle,
                              description=chunk,
                              color=discord.Color.blurple(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=songThumbnail)
        embed.set_footer(text=f"Song by {songArtist}")
        await ctx.send(embed=embed)


@client.command()
async def meta(ctx):
    embed = discord.Embed(title="Meta of codm [SEASON : 7]",
                          description="",
                          colour=discord.Color.blue())

    embed.add_field(
        name="1. HOLGER",
        value=
        "The weapon appears in Call of Duty: Mobile as the Holger 26. It was added in June 2021 as part of the Season 4: Spurned & Burned update.",
        inline=False)
    embed.add_field(
        name="2. MX9",
        value=
        "The MX9 returns in Call of Duty: Mobile. It was added in July 2021 as part of the Season 6: The Heat update.",
        inline=False)
    embed.add_field(
        name="3. PP19",
        value=
        "The PP19 Bizon returns in Call of Duty: Mobile. It was added in April 2021 as part of the Season 3: Tokyo Escape update.",
        inline=False)
    embed.add_field(
        name="4. QQ9",
        value=
        "The MP5 returns in Call of Duty: Mobile as the QQ9. It was added as part of the Season 7 Radioactive Agent update.",
        inline=False)
    embed.add_field(
        name="5. AS VAL",
        value=
        "The AS VAL appears in Call of Duty: Mobile. It was added in March 2021 as part of the Season 2: Day of Reckoning update.",
        inline=False)

    await ctx.send(embed=embed)


@client.command()
async def purge(ctx, *, limit: int):
    limit = int((limit + 1))
    await ctx.channel.purge(limit=limit)
    purge_limit = limit - 1
    await ctx.send(f"{purge_limit} messages purged by {ctx.author.mention}",
                   delete_after=1)


@purge.error
async def zooomba(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        embed = discord.Embed(title=(
            "Number of messages is a required argument which is missing!!"),
                              description=(
                                  "Format: `-purge {number of messages}`"),
                              colour=discord.Color.blue())
        await asyncio.sleep(1)
        await ctx.send(embed=embed)


@client.command(name="8ball")
async def ball(ctx, *, question: str):
    ball = [
        "According to my calculations, I say YES!",
        "IS that even a goddamn question? Ofcourse NO!", "Absolutely!",
        "My sources say yes!", "Maybe I dont know!!!", "Yes ig....", "Nah..",
        "Not sure tbh", "Fuck yeah..", "My sources say No", "Yesn't",
        "All odds are again you so **NO**", "Nope!!", "Ask monke god instead- I am not sure about this.."
    ]
    embed = discord.Embed(title=f"{ctx.author.name} asks {question}",
                          description=(random.choice(ball)))
    await ctx.send(embed=embed)


@client.command()
async def avatar(ctx, *, member: discord.Member = None):
    embed = discord.Embed(title="User avatar",
                          description=f"User avatar of {member} ",
                          colour=discord.Color.blue())
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)


@client.command()
async def codmreddit(ctx):
    await ctx.send("Command is disabled due to some errors. Have patience kek")





@client.command()
@has_permissions(manage_messages=True)
async def lock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(
        title=f"Locked <:lock:888363185109864450>",
        description=f"{channel} has been locked by {ctx.author.mention}")
    await ctx.send(embed=embed)


@client.command()
async def unlock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(
        title=f"Unlocked <:unlock:888362821409193994>",
        description=f"{channel} has been locked by {ctx.author.mention}",
        colour=discord.Color.gold())
    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
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
    await ctx.send('Press the button!', view=view)


@client.command()
async def sike(ctx):
    class MyView(discord.ui.View):
        @discord.ui.button(label="", style=discord.ButtonStyle.primary)
        async def button_callback(self, button, interaction):
            button.disabled = True
            button.label = 'No more pressing!'
            await interaction.response.edit_message(view=self)





@client.command()
async def press(ctx):
    class MyView(discord.ui.View):
        @discord.ui.button(label='A button', style=discord.ButtonStyle.primary)
        async def button_callback(self, button, interaction):
            button.disabled = True
            button.label = 'No more pressing!'
            await interaction.response.edit_message(view=self)

    view = MyView()
    await ctx.send('Press the button!', view=view)



@client.command()
@commands.has_permissions(administrator=True)
async def timer(ctx, timeInput = None, str = None):
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]      
        if time > 86400:
            await ctx.send("I can\'t do timers over a day long")
            return
        if time <= 0:
            await ctx.send("Timers don\'t go into negatives :/")
            return
        if time >= 3600:
            embed = discord.Embed(
              title = "Timer",
              description = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
            )
            message = await ctx.send(embed=embed)
        elif time >= 60:
            embed = discord.Embed(
              title = "Timer",
              description = f"Timer: {time//60} minutes {time%60} seconds")
            message = await ctx.send(embed=embed)
        elif time < 60:
            embed = discord.Embed(
              title = "Timer",
              description = f"Timer: {time} seconds")
            message = await ctx.send(embed=embed)
        while True:
            try:
                await asyncio.sleep(5)
                time -= 5
                if time >= 3600:
                    embed.description(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
                    await message.edit(embed = embed)
                elif time >= 60:
                    embed.description(content=f"Timer: {time//60} minutes {time%60} seconds")
                    await message.edit(embed = embed)
                elif time < 60:
                    embed.description(content=f"Timer: {time} seconds")
                    await message.edit(embed=embed)
                if time <= 0:
                    await message.edit(content="Ended!")
                    await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
                    break
            except:
                break
    except:
        await ctx.send(f"hoi")

@client.command(pass_context=True)
async def codingmeme(ctx):
    embed = discord.Embed(title="", description="")
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Coding/new.json?sort=meme') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
@client.command()
async def fetchcmnd(ctx):
  for command in client.commands:
    await ctx.send(command)

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    em = discord.Embed(
      title = f"Last deleted message in #{channel.name}", 
      description = snipe_message_content[channel.id])
    em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
    await ctx.send(embed = em)

@client.command()
async def spotify(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author
    pass
  if user.activities:
    for activity in user.activities:
      if isinstance(activity, Spotify):
        embed = discord.Embed(
            title = f"{user.name}'s Spotify",
            description = "Listening to {}".format(activity.title),
            color = 0xC902FF)
        embed.set_thumbnail(url=activity.album_cover_url)
        embed.add_field(name="Artist", value=activity.artist)
        embed.add_field(name="Album", value=activity.album)
        embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
        await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
      await ctx.send("Missing required arguments! \n Reform the command in proper format!")
    await client.process_commands(error)

    

@client.event
async def on_message(message):
  if 'suicide' in message.content:
      embed = discord.Embed(
          title=" Need help?",
          description=
          "Oh hi! Retro here just noticed a word a word which might be related to self harm \n If it is not please ignore it. But if it is, please consider reading it.",
          colour=discord.Color.gold())
      embed.add_field(
          name="Its gonna be alright!",
          value=
          "Im not a therapist and you dont even know me but trust me it getts better with time. It might take a lot of time but there is a beautiful city on the other end of the sea.",
          inline=False)
      embed.add_field(
          name="Tell someone who loves you",
          value=
          "Have the courage to speak up to someone! Its fine. It might be hard but trust me! Once you say it to someone you are gonna feel much better. It doesnt matter who it is online friend, IRL friend, parents, cousin anyone. The person who can help you more than a therapist is a person who knows you very well.",
          inline=True)
      embed.add_field(
          name=
          "Don't have anyone to talk to? Are you scared of being judged?",
          value=
          "Talk to me AKA Retro#9588, I dont know you but thats better, I wont be able to judge you on your past or present.",
          inline=False)
      embed.add_field(
          name="Suicide is never a right decision",
          value=
          "Do you know, most of the survivors who jumped from the Golden Gate Bridge regret their choice. Do you really want to regret your life-ending decision and regret it but its nevertheless too late! \n Do you know you might end your TEMPORARY PROBLEM with suicide but give your family and your close friends PERMANENT TRAUMA and SADNESS \n No one really likes to see their children hanging from a fan and jumping from a building right? ",
          inline=True)
      embed.add_field(
          name="Suicide hotline numbers",
          value=
          """If nothing works out for you, consider calling suicide helpine of your specific country, they will surely try to help you. \n Hotlines numbers: \n [India](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm)  : 8888817666
          \n[USA](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm): 1-800-273-8255 
          \n [UK](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : 0800 689 5652 
          \n[South Korea](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : (02) 7158600 
          \n [Denmark](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) :  4570201201 
          \n[Canada](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : 1 (833) 456 4566 
          \n [Australia](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : 1 (833) 456 4566 
          """,
          inline=False)
      await message.author.send(embed=embed)
      embed = discord.Embed(
        title = "Suicide helpine numbers",
        description = """If nothing works out for you, consider calling suicide helpine of your specific country, they will surely try to help you. \n Hotlines numbers: \n [India](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm)  : 8888817666
          \n[USA](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm): 1-800-273-8255 
          \n [UK](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : 0800 689 5652 
          \n[South Korea](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : (02) 7158600 
          \n [Denmark](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) :  4570201201 
          \n[Canada](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : 1 (833) 456 4566 
          \n [Australia](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : 1 (833) 456 4566 
          \n [Switzerland](https://www.helpguide.org/articles/suicide-prevention/are-you-feeling-suicidal.htm) : """

      )
  await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, discord.ext.commands.errors.CommandNotFound):
    embed1=discord.Embed(
      title="<:dl_tick_nah:899182950283898890> **Action failed**", 
      description="Sorry, that command does not exist! \n Use `a!help` to look at all the commands!", color=0xCBC3E3)
    embed1.set_footer(text=f"Find any errors? Report it to the support server!")
    await ctx.reply(embed=embed1)
    await client.process_commands(error)

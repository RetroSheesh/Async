import discord
from discord.ext import commands
import random
import asyncio


class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def coinflip(self, ctx):
    determine_flip = ["heads", "tails"]
    if random.choice(determine_flip) == "heads":

      embed = discord.Embed(
        title="Flipping a coin...",
        description=f"{ctx.author.mention} Flipped coin, we got **Heads**!"
        )
      await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
          title="Coinflip | Async",
          description=f"{ctx.author.mention} Flipped coin, we got **Tails**!"
        )
        await ctx.send(embed=embed)
  @commands.command()
  async def echo(ctx, *, content: str):
      embed = discord.Embed(title=(""),
                            description=(f"{content}"),
                            colour=discord.Color.red())
      embed.set_footer(text=f"Requested by {ctx.author.name} ")

      await ctx.reply(embed=embed)


  @echo.error
  async def on_error(ctx, error):
    embed = discord.Embed(
        title=("Content is a required argument which is missing!!"),
        description=("Format: `-echo {content}`"),
        colour=discord.Color.blue())

    embed.set_footer(text="What do you actually want me to say!!")
    await ctx.send(embed=embed)

  @commands.command()
  async def pp(ctx, member: discord.Member = None):
    peepee = [
    "You dont have one lmfao", "8D", "8=D", "8==D", "8===D", "8====D",
    "8=====D", "8======D", "8======D", "8=======D", "8========D",
    "8=========D", "8==========D", "8===========D", "8============D",
    "8=============D", "8==============D", "8===============D"
]
    if member == None:
        embed = discord.Embed(title=(f"{ctx.author.name} pp size"),
                              description=(random.choice(peepee)),
                              colour=discord.Colour.dark_gold())
        embed.set_footer(text="")
        await ctx.send(embed=embed)
    else:
        embed5 = discord.Embed(title=(f"{member.name} PP size'"),
                               description=(random.choice(peepee)),
                               colour=discord.Colour.red())
    embed5.set_footer(text="Sussy")
    await ctx.send(embed=embed5)




  @commands.command()
  async def truth(ctx, *, member: discord.Member = None):
    truth_commands = (
  "What's the most embarrassing top-played song on your phone?",
  "What was your favorite childhood show?",
  "If you could be a fictional character for a day",
  "What's your biggest fear?",
  "What's one silly thing you can't live without?",
  "What is the weirdest trend you've ever participated in?",
  "If you could only listen to one song for the rest of your life what would you choose?",
  "What person do you text the most?",
  "Have you ever been fired from a job?",
  "What is an instant deal breaker in a potential love interest?",
  "If you could only eat one thing for the rest of your life",
  "what would you choose?",
  "What is the biggest lie you ever told your parents?",
  "What's the worst physical pain you've ever experienced?",
  "Which player knows you the best?",
  "What's your favorite part of your body?",
  "What's the weirdest thing you've ever eaten?",
  "Have you ever gone skinny dipping?",
  "Tell us about the worst date you've ever been on?",
  "Who is your celebrity crush?",
  "What's the strangest dream you've ever had?",
  "What are the top three things you look for in a boyfriend/girlfriend?",
  "What is your worst habit?", "How many stuffed animals do you own?",
  "What is your biggest insecurity?",
  "What was the last thing you searched for on your phone?",
  "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read which would you choose?",
  "Have you ever walked in on your parents doing it?",
  "After you've dropped a piece of food",
  "what's the longest time you've left it on the ground and then ate it?",
  "Have you ever tasted a booger?",
  "Have you ever played Cards Against Humanity with your parents?",
  "What's the first thing you would do if you woke up one day as the opposite gender?",
  "Have you ever peed in the pool?",
  "Who do you think is the worst-dressed person in this room?",
  "Have you ever farted in an elevator?", "Of the people in this chat",
  "who do you want to trade lives with?",
  "What are some things you think about when sitting on the toilet?",
  "Did you have an imaginary friend growing up?",
  "Do you cover your eyes during a scary part in a movie?",
  "Have you ever practiced kissing in a mirror?",
  "Did your parents ever give you the birds and the bees talk?",
  "What is your guilty pleasure?", "What is your worst habit?",
  "Has anyone ever walked in on you when going in the bathroom?",
  "Have you ever had a wardrobe malfunction?",
  "Have you ever walked into a wall?", "Do you pick your nose?",
  "Do you sing in the shower?", "Have you ever peed yourself?",
  "What was your most embarrassing moment in public?",
  "Have you ever farted loudly in class?",
  "Do you ever talk to yourself in the mirror?",
  "You’re in a public restroom and just went 2 then you realized your stall has no toilet paper. What do you do?",
  "What would be in your web history that you’d be embarrassed if someone saw?",
  "Have you ever tried to take a sexy picture of yourself?",
  "Do you sleep with a stuffed animal?"
  "Do you drool in your sleep?", "Do you talk in your sleep?",
  "Who is your secret crush?", "Do you think  is cute?",
  "Who do you like the least in this room and why?",
  "What does your dream boy or girl look like?",
  "What is your go-to song for the shower?",
  "Who is the sexiest person in this room?",
  "How would you rate your looks on a scale of 1 to 10?",
  "You dont deserve a truth", "What don't you like about me?",
  "What color underwear are you wearing right now?",
  "What was the last thing you texted?",
  "If you were rescuing people from a burning building and you had to leave one person behind from this room",
  "who would it be?",
  "Do you think you'll marry your current girlfriend/boyfriend?",
  "How often do you wash your undergarments?",
  " Have you ever tasted ear wax?",
  "Have you ever farted and then blamed someone else?",
  "Would you wear your shirt inside out for a whole day if someone paid you $100?",
  "What is the most childish thing that you still do?",
  "How far would you go to land the guy or girl of your dreams?",
  "Tell us about a time you embarrassed yourself in front of a crush.",
  "Have you ever kept a library book?",
  "Who is one person you pretend to like but actually don’t?",
  "What children’s movie could you watch over and over again?",
  "Do you have bad foot odor?", "Do you have any silly nicknames?",
  "When was the last time you wet the bed?",
  "How many pancakes have you eaten in a single sitting?",
  "Have you ever accidentally hit something with your car?",
  "If you had to make out with any Disney character who would it be?",
  "Have you ever watched a movie you knew you shouldn’t?",
  "Have you ever wanted to try LARP (Live Action Role-Play)?",
  "What app on your phone do you waste the most time on?",
  "Have you ever pretended to be sick to get out of something? If so what was it?",
  "What is the most food you’ve eaten in a single sitting?",
  "Do you dance when you’re by yourself?",
  "Would you have voted for or against Trump?",
  "What song on the radio do you sing with every time it comes on?",
  "Do you sleep with a stuffed animal?",
  "Do you own a pair of footie pajamas?", "Are you scared of the dark?",
  "What as seen on TV product do you secretly want to buy?",
  "Do you still take bubble baths?",
  "If you were home by yourself all day what would you do?",
  "How many selfies do you take a day?",
  "What is something you’ve done to try to be ‘cooler’?",
  "When was the last time you brushed your teeth?",
  "Have you ever used self-tanner?",
  "What do your favorite pajamas look like?",
  "Do you have a security blanket?",
  "Have you ever eaten something off the floor?",
  "Have you ever butt-dialed someone?") 
    if member == None:
        member = ctx.author

    embed4 = discord.Embed(title=(f"{ctx.author.name} asks {member.name}"),
                          description=(random.choice(truth_commands)),
                          colour=discord.Color.blue())
    await ctx.send(embed=embed4)
  @commands.command()
  async def howgay(self, ctx):
    random_number3 = random.randint(1, 100)
    embed = discord.Embed(
        title="Gay rate machine ",
        description=(f"you are {random_number3}% gay :rainbow_flag: "),
        colour=discord.Color.blue())
    await ctx.send(embed=embed)


  @commands.command()
  async def single(ctx):
      random_number3 = random.randint(0, 100)
      embed = discord.Embed(
          title="Single rate machine ",
          description=
          (f"you are {random_number3}% single <:icetealonely:885476663528411158> "
          ),
          colour=discord.Color.blue())
      if random_number3 == "0":
          await ctx.send("Try your luck! You might just get a partner today :))")
      await ctx.send(embed=embed)


  @commands.command()
  async def respect(ctx):
      random_number = random.randint(1, 100)
      embed2 = discord.Embed(
          title="Respect RATE",
          description=(f"you have {random_number}% of respect"),
          colour=discord.Color.blue())
      embed2.set_footer(text="Imagine having only that much respect")
      await ctx.send(embed=embed2)
  @commands.command()
  async def personality(self, ctx):
      personalityhehe = random.randint(1, 100)
      apersonalityhehe = random.randint(1, 100)
      bpersonalityhehe = random.randint(1, 100)
      cpersonalityhehe = random.randint(1, 100)
      dpersonalityhehe = random.randint(1, 100)
      epersonalityhehe = random.randint(1, 100)
      fpersonalityhehe = random.randint(1, 100)
    
      message = await ctx.send("Personality check...", delete_after=15)
      await message.edit(content="Checking past records....")
      await asyncio.sleep(1)
      await message.edit(content="Checking relations with friends and relatives")
      await asyncio.sleep(1)
      await message.edit(content="Checking loyalty....")
      await asyncio.sleep(1)
      await message.edit(content="Checking atiques and respect to others...")
      await asyncio.sleep(1)
      await message.edit(content="Final checking")
      await asyncio.sleep(1)
      await message.edit(content="Posting results in ")
      await message.edit(content="3")
      await message.edit(content="2")
      await message.edit(content="1")
      embed = discord.Embed(
        title=" Personality test",
        description="")
      embed.add_field(name="Loyalty", value = f"{personalityhehe}%")
      embed.add_field(name="Criminal mind", value = f"{bpersonalityhehe}%")
      embed.add_field(name="Gayness", value = f"{cpersonalityhehe}%")
      embed.add_field(name="Lazy", value = f"{dpersonalityhehe}%")
      embed.add_field(name="Respect for others", value = f"{epersonalityhehe}%")
      embed.add_field(name="Depressed", value = f"{fpersonalityhehe}%")
      embed.add_field(name="Manners", value = f"{apersonalityhehe}%")
      await ctx.send(embed=embed)
  @commands.command()
  async def userinfo(self, ctx, *, member3:discord.Member):


    embed = discord.Embed(
      title=f"Userinfo of {member3} ",
      description=" ",
      colour=discord.Color.red())
    embed.add_field(name="Username with discriminator", value = member3.name)
    embed.add_field(name="User ID", value = member3.id)
    embed.add_field(name="User created at",
                    value=member3.created_at.strftime("%B %d %Y"))
    embed.add_field(name="User joined at",
                    value=member3.joined_at.strftime("%B %d %Y"))

    embed.add_field(name="Highest role of user", value=f"{member3.top_role}")
    embed.add_field(name="All  roles of the user", value = f"Roles are ")
  @commands.command()
  async def rps(self, ctx):
    lol = ["Rock 🪨", "Scissors 🗡️", "Paper 🧻"]
    lolman = random.choice(lol)
    await ctx.send("Rock , Paper or Scissors?")

    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author

    msg = await self.bot.wait_for('message', check=check)
    if lolman == "Rock 🪨" and msg.content == "rock":
        await ctx.send("I choose ROCK!! 🪨")
        await ctx.send("Damn , thats a tie")
    elif lolman == "Scissors 🗡️" and msg.content == "scissors":
        await ctx.send("I choose Scissors")
        await ctx.send("Damn , thats a tie :(")
    elif lolman == "Paper 🧻" and msg.content == "paper":
        await ctx.send("Paper 🧻")
        await ctx.send("Damn , thats a tie :(")
    elif lolman == "Rock 🪨" and msg.content == "scissors":
        await ctx.send("Rock 🪨!")
        await ctx.send("I WON LETS GOOO")
    elif lolman == "Rock 🪨" and msg.content == "paper":
        await ctx.send("Rock 🪨!")
        await ctx.send("Damn!You won this round!GG :D")
    elif lolman == "Scissors 🗡️" and msg.content == "paper":
        await ctx.send("Scissors 🗡️")
        await ctx.send("I WON LETS GOOO")
    elif lolman == "Scissors 🗡️" and msg.content == "rock":
        await ctx.send("Scissors 🗡️!")
        await ctx.send("Nooo :( GG bro")
    elif lolman == "Paper 🧻" and msg.content == "rock":
        await ctx.send("Paper 🧻")
        await ctx.send("I WON LETS GOOO")
    elif lolman == "Paper 🧻" and msg.content == "scisssors":
        await ctx.send("Paper 🧻!")
        await ctx.send("Nooo :( GG bro")
  @commands.command()
  async def gf(self, ctx, memberig: str = None):
      random_number3 = random.randint(1, 100)
      embed = discord.Embed(
          title="Couple rating",
          description=f"{memberig} has an {random_number3}% chance to get a gf",
          colour=discord.Color.gold())
      embed.set_footer(text="UwU")
      embed.set_thumbnail(
          url=
          "https://o.remove.bg/downloads/8c9716b4-1922-404d-a0e8-82f7a2442302/images-removebg-preview.png"
      )
      await ctx.send(embed=embed)

  @commands.command()
  async def hack(self, ctx, member: discord.Member):
    password = [
        "Moneyforme?2", "Yeet120", "Booknerd", "Bully101", "qwertyboi",
        "discordusergod", "man99", "jokeyman234", "heheboi7634",
        "MyExBrokeUpWithMe6969", "Hehehe453", "Nonosir23", "YouYeet@420",
        "rikrombl23", "Passwordbuttaken", "shfffw203"
    ]
    dm = [
        "Hey Mom Whats for dinner today",
        "Hey Derek , can u help me cheat with the test",
        "Yes dada , i finished my homework",
        "Bye Babe, i wont tell my parents im going to your house ",
        "LOL bro that was fun see ya!",
        "MY guy!Ok then, ill see ya tmw",
        "Bruh did you hear the gossip , Marianne likes you and painted your name and a heart on her body",
        "Nice talking to you man",
        "NOOO",
        "DONT U DARE BLOCK ME, give me the nitro ",
        "Yooo can we-",
        "I am sorry I was trying to tell you but....",
        "220hgeuvg",
    ]
    message = await ctx.send(f"Hacking {member.mention} ")
    await asyncio.sleep(1)
    await message.edit(content=f"Retrieving Email of {member.mention} ")
    await message.edit(content=f"Retrieved Email of {member.mention} ")
    await asyncio.sleep(1)
    await message.edit(content=f"Found the Password of {member.mention} ")
    await asyncio.sleep(1)
    await message.edit(content=f"Retrieved Latest DMs from {member} ")
    await asyncio.sleep(1)
    await message.edit(content=f"Sending data to Retro and team")
    await message.edit(content="Data sent!")
    embed = discord.Embed(title='The unbelievable hack is complete')
    numbers = random.randint(1, 100)

    embed.add_field(name=f"Email of {member} :",
                    value=f"{member.display_name}{numbers}@gmail.com")
    embed.add_field(name="Password:", value=random.choice(password))
    embed.add_field(name="Latest DM msg:", value=random.choice(dm))
    await ctx.send(embed=embed)


  @commands.command()
  async def rate(self, ctx, member: str, *, member2: str):
    random_number3 = random.randint(1, 100)
    embed = discord.Embed(
        title="Couple rating",
        description=
        f"{member} and {member2} are {random_number3} % compatible",
        colour=discord.Color.gold())
    embed.set_footer(text="Uwu")
    embed.set_thumbnail(
        url=
        "https://o.remove.bg/downloads/8c9716b4-1922-404d-a0e8-82f7a2442302/images-removebg-preview.png"
    )
    await ctx.send(embed=embed)
def setup(bot):
  bot.add_cog(Fun(bot))

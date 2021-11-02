import discord
from discord.ext import commands


class Gunsmith(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def gunsmith(self, ctx, gun: str = None):
    if gun == None:
      await ctx.send(f"Please mention a gun, {ctx.author.mention}!")
    if gun == "kn44":
        embed = discord.Embed(
          title = ("KN44 GUNSMITH"),
          description = ("KN44"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : BLOOD OK#0588")
        embed.set_thumbnail(url="https://pasteboard.co/Kiqk3UW.png")
        embed.set_image(url="https://media.discordapp.net/attachments/879390150227025921/882461739051012186/image0.png?width=904&height=678")
        await ctx.send(embed=embed)
    
    if gun == "drh":
        embed = discord.Embed(
          title = ("DRH GUNSMITH"),
          description = ("DRH"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro#1357 ")
        embed.set_image(url="https://media.discordapp.net/attachments/879747536334774324/883694485287108648/image0.png?width=904&height=678")
        await ctx.send(embed=embed)

    if gun == "crossbow":

        embed = discord.Embed(
          title = ("Crossbow GUNSMITH"),
          description = ("Crossbow"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : path.exe#0915")
        embed.set_image(url="https://cdn.discordapp.com/attachments/785461568464748593/882503628538126336/image0.png")
        await ctx.send(embed=embed)

    if gun == "na45":


        embed = discord.Embed(
          title = ("NA45 GUNSMITH"),
          description = ("NA45"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro#1357")
        embed.set_image(url="https://cdn.discordapp.com/attachments/881725910649290762/883648752932487188/SPOILER_async.png")
        await ctx.send(embed=embed)
        await ctx.author.send("Hey, stop using NA45 and please do something better with your lelife ")

    if gun == "dlq33":

        embed = discord.Embed(
          title = ("DLQ33 GUNSMITH"),
          description = ("DLQ33"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro#1357")
        embed.set_image(url="https://cdn.discordapp.com/attachments/879747536334774324/883692080373858324/image0.png")
        await ctx.send(embed=embed)
          
    if gun == "mx9":

        embed = discord.Embed(
          title = ("MX9 GUNSMITH"),
          description = ("MX9"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro")
        embed.set_image(url="https://gcdn.pbrd.co/images/s7HxPEJ6i53a.png?o=1")
        await ctx.send(embed=embed)

    if gun == "asval":

        embed = discord.Embed(
          title = ("ASVAL GUNSMITH"),
          description = ("AS VAL"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro")
        embed.set_image(url="https://media.discordapp.net/attachments/880641264431804506/883673999031271484/image0.png?width=904&height=678")
        await ctx.send(embed=embed)

    if gun == "outlaw":

        embed = discord.Embed(
          title = ("OUTLAW GUNSMITH"),
          description = ("OUTLAW"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro")
        embed.set_image(url="https://media.discordapp.net/attachments/879747536334774324/883676077518622730/image2.png?width=904&height=678")
        await ctx.send(embed=embed)

    if gun == "locus":

        embed = discord.Embed(
          title = ("LOCUS GUNSMITH"),
          description = ("LOCUS GUNSMITH"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro")
        embed.set_image(url="https://media.discordapp.net/attachments/879747536334774324/883676076985958410/image1.png?width=904&height=678")
        await ctx.send(embed=embed)

    if gun == "krm":

        embed = discord.Embed(
          title = ("KRM 262 GUNSMITH"),
          description = ("KRM 262"),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro")
        embed.set_image(url="https://media.discordapp.net/attachments/879747536334774324/883676078097465384/image3.png?width=904&height=678")
        await ctx.send(embed=embed)

    if gun == "chopper":

        embed = discord.Embed(
          title = ("CHOPPER GUNSMITH"),
          description = ("CHOPPER "),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Retro")
        embed.set_image(url="https://images-ext-2.discordapp.net/external/AvnS0Dvzf3iXj1hKE7HReeUaemsCYZwypJYQPhdhY8k/%3Fwidth%3D904%26height%3D678/https/media.discordapp.net/attachments/879747536334774324/883676078525251614/image4.png?width=866&height=650")
        await ctx.send(embed=embed)

    if gun == "pp19":

        embed = discord.Embed(
          title = ("PP19 GUNSMITH"),
          description = ("PP19 "),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Blood")
        embed.set_image(url="https://media.discordapp.net/attachments/879747536334774324/883714027774156861/pp19.jpg")
        await ctx.send(embed=embed)

    if gun == "qxr":

        embed = discord.Embed(
          title = ("QXR GUNSMITH"),
          description = ("QXR "),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Blood")
        embed.set_image(url="https://media.discordapp.net/attachments/879747536334774324/883714027774156861/pp19.jpg")
        await ctx.send(embed=embed)

    if gun == "hso405":

        embed = discord.Embed(
          title = ("HSO GUNSMITH"),
          description = ("HSO "),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Godzly")
        embed.set_image(url="https://gcdn.pbrd.co/images/WKKNCsLoLvSL.png?o=1")
        await ctx.send(embed=embed)

    if gun == "shorty":

        embed = discord.Embed(
          title = (" SHORTY GUNSMITH"),
          description = ("SHORTY "),
          colour = discord.Color.blue())
        embed.set_footer(text= "Gunsmith Credit : Godzly")
        embed.set_image(url="https://gcdn.pbrd.co/images/dhF3KWWobIZf.png?o=1")
        await ctx.send(embed=embed)

    if gun == "ak117":
        embed = discord.Embed(
          title = ("AK117 GUNSMITH"),
          description = ("AK117"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : NoahFromYT")
        embed.set_image(url="https://gcdn.pbrd.co/images/XLUMjV0LEBfW.png?o=1")
        await ctx.send(embed=embed)
    if gun == "qq9":
        embed = discord.Embed(
          title = ("qq9 GUNSMITH"),
          description = ("qq9"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : NoahFromYT")
        embed.set_image(url="https://gcdn.pbrd.co/images/kgUqFs5mIVF4.png?o=1")
        await ctx.send(embed=embed)
    if gun == "peacekeeper":
        embed = discord.Embed(
          title = ("Peacekeeper GUNSMITH"),
          description = ("PEACEKEEPER"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Ice COD:M")
        embed.set_image(url="https://gcdn.pbrd.co/images/01OEWR7uwSeS.png?o=1")
        await ctx.send(embed=embed)
#https://media.discordapp.net/attachments/744223911029375037/887958588893577236/Screenshot_20210914-180148_Call_of_Duty.jpg?width=1441&height=648    
    if gun == "msmc":
        embed = discord.Embed(
          title = ("MSMC GUNSMITH"),
          description = ("MSMC"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Ontarage7#9692")
        embed.set_image(url="https://media.discordapp.net/attachments/744223911029375037/887958588893577236/Screenshot_20210914-180148_Call_of_Duty.jpg?width=1441&height=648")
        await ctx.send(embed=embed)
    if gun == "msmc":
        embed = discord.Embed(
          title = ("MSMC GUNSMITH"),
          description = ("MSMC"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Ontarage7#9692")
        embed.set_image(url="https://media.discordapp.net/attachments/744223911029375037/887958588893577236/Screenshot_20210914-180148_Call_of_Duty.jpg?width=1441&height=648")
        await ctx.send(embed=embed)
    if gun == "holger":
        embed = discord.Embed(
          title = ("HOLGER GUNSMITH"),
          description = ("HOLGER"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Blood ")
        embed.set_image(url="https://media.discordapp.net/attachments/852936304039428127/889717314646327356/image0.png?width=904&height=678")
        await ctx.send(embed=embed)
    if gun == "mow":
        embed = discord.Embed(
          title = ("HOLGER GUNSMITH"),
          description = ("HOLGER"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Blood ")
        embed.set_image(url="https://media.discordapp.net/attachments/852936304039428127/889718984298098708/image0.png?width=904&height=678")
        await ctx.send(embed=embed)
    if gun == "agr":
        embed = discord.Embed(
          title = ("AGE GUNSMITH"),
          description = ("AGR"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Blood ")
        embed.set_image(url="https://media.discordapp.net/attachments/852936304039428127/889720371513798676/image0.png?width=904&height=678")
        await ctx.send(embed=embed)
    if gun == "rus":
        embed = discord.Embed(
          title = ("RUS GUNSMITH"),
          description = ("RUS"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Jokesta ")
        embed.set_image(url="https://media.discordapp.net/attachments/879390150227025921/889872275145367552/unknown.png")
        await ctx.send(embed=embed)
    if gun == "rus":
        embed = discord.Embed(
          title = ("RUS GUNSMITH"),
          description = ("RUS"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Jokesta ")
        embed.set_image(url="https://media.discordapp.net/attachments/879390150227025921/889872275145367552/unknown.png")
        await ctx.send(embed=embed)
    if gun == "asm10":
        embed = discord.Embed(
          title = ("ASM10 GUNSMITH"),
          description = ("ASM"),
          colour = discord.Color.blue())
        embed.set_footer(text="Gunsmith credit : Blood ")
        embed.set_image(url="https://media.discordapp.net/attachments/887593043081969705/890256478018097153/image0.png?width=904&height=678")
        await ctx.send(embed=embed)
def setup(bot):
  bot.add_cog(Gunsmith(bot))

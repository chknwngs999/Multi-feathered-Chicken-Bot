#pycharm, eclipse, sublime, vscode, etc
import discord, os
from dotenv import load_dotenv
from discord.ext import commands, tasks

#from testcommandimport import hangCheckLetter

import requests
from discord import Webhook, RequestsWebhookAdapter, File#webhook = Webhook.partial(774519149031587861, 'nnKtLPKXpVWCBznbahR47VGwyHGFCaaoP1VzZlmhYzRcKVbDz7hXY1n6tR3h13Wldkxq', adapter=RequestsWebhookAdapter()) webhook.send('The Ancient One has awakened.')

#import cogs
#logs with txt files? (codecademy read/write to txt) or pickle stuff?

import random
import asyncio
from datetime import datetime, timezone, timedelta
import pytz

#+/- flipped! (timezone is how far ahead is gmt from other timezone?)
timezone = pytz.timezone("Etc/GMT+8")
padoruday = datetime.strptime('12 25 21 08:00 -0800', '%m %d %y %H:%M %z')

import keep_alive
intents = discord.Intents.all()
intents.members = True  # Subscribe to the privileged members intent.
#https://discordpy.readthedocs.io/en/latest/intents.html


#usable - member, message.author, guild.id/name, client.user (bot), message.content, ctx.message(.delete)/get_channel/author/.id get_user doesn't work (client v bot?)
#bot.user.name/discriminator, bot.guilds, bot.get_all_channels()
#guild.members.name/discriminator
#parameter: dt=default
#message.id/channel/name/position/nsfw/news/id/type/author/(name/discriminator)/bot/nick/guild/name/content (to check all properties just do print(message) in something like on delete ( also applies to before/after in on edit))
#channel = discord.utils.get(bot.get_all_channels(), name="welcome-goodbye")
#emoji = discord.utils.get(guild.emojis, name='LUL')
#remove_mentions(string)
#discord.utils.get/find
#bot.get_channel?
#default_role

#no need for database for levels/num commands/total users, USE PICKLE

load_dotenv() #what does this do
bot = commands.Bot(command_prefix="-", case_insensitive = True, intents=intents, help_command=None)
#https://stackoverflow.com/questions/62644195/discord-py-change-the-default-help-command
token = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

sniped = []
snipeauthor = []
esniped = []
esnipe_change = []
esnipeauthor = []
guild = ""

#repurpose functions to await ctx.send("") instead of print
#repurpose update to be embed FUTURE
def hangCheckLetter(letter: str):
  global guessed, guesses, wrong, within, response, used
  within = False
  if letter.lower() not in used:
    used.append(letter.lower())
    guesses += 1
    for i in range(len(anime)):
      if anime[i].lower() == letter.lower():
        guessed[i] = True
        within = True
        response = (f"The letter {letter} was in the term. Guess another letter.")
    if within == False:
      wrong += 1
      response =(f"The letter {letter} is not in the term.")
  else:
    response = "You already guessed that letter."
  if wrong > 0:
    response += f"\nYou have guessed wrong {wrong} times. {6-wrong} more before you lose."
def hangUpdate():
  global updatemessage, anime, guessed
  updatemessage = ""
  for i in range(len(anime)):
    if guessed[i] == True or anime[i].lower() not in letters:
      updatemessage += anime[i] + " "
    elif anime[i] == " ":
      updatemessage += "  "
    else:
      updatemessage += "\_ "
  return updatemessage
def checkCompletion():
  global guessed, gameon
  finished = False
  for i in guessed:
    if i != True:
      return False
    else:
      pass
  gameon = False
  return True

#check if all of guessed is true
#send list of letters used
#reset variables when completed
#error handling incorrect letters
#deal with dashes and other punctuation like spaces
#check completion within other function
#hangman not ended after entire term guessed
#sending different messsage if completed
#handle all in function
#do i even need function
#embeds, show used letters
#toggle japanese (ending thing english/japanese/all, default english)
#clean up/improve code

#remove guessed, just compare anime[i] with used
gameon = False
anime = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

within = False
guessed = []
used = []

guesses = 0
wrong = 0

updatemessage = ""
response = ""

#Events
#booting messages (username, guild, members)
@bot.event
async def on_ready():
  global guild
  guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
  #or guild = discord.utils.get(bot.guilds, name=GUILD)
  print(f'{bot.user.name}#{bot.user.discriminator} is connected to to the following guild:\nBot User ID: {bot.user.id}\n{guild.name}(id: {guild.id})\n')
  
  await bot.change_presence(activity=discord.Game(f"Struggling to survive in {len(bot.guilds)} servers [-help]"))
  #if you need to check for properties
  
  #print(guild.members)
  #print(bot.guilds)

  for guild in bot.guilds:
    #convert to dict with "member": discrim
    membersList = [member.name for member in guild.members]
    discrimList = [discriminator.discriminator for discriminator in guild.members]
    #membersDict = {member.name: discriminator.discriminator for member, discriminator in guild.members}
    print(f"\n-{guild} has {guild.member_count} members.") #guild.channels
    for i in range(len(membersList)):
      print(f"- - {membersList[i]}#{discrimList[i]}")
  
  """today = timezone.localize(datetime.now())
  while today != padoruday:
    today = timezone.localize(datetime.now())
  else:
    announce = discord.utils.get(bot.get_all_channels(), "announcements")
    announce.send("MERRY PADORU EVERYBODYYYYY.")"""

  #channel = discord.utils.get(bot.get_all_channels(), name="announcements")
  #await channel.send("yoyoyo, wake up.")

  #print(f'Guild Members:\n - {members}') #this line + prev line list members (broken?)

#join message(use embeds) (change with a command? - check role, set variable strings with gifs/messages, then f"" in on_member_join)
@bot.event
async def on_member_join(member):
  print(f"{member.mention} joined!")
  general = discord.utils.get(bot.get_all_channels(), name="general")#general id - 742258921733095437
  embed=discord.Embed(title="Welcome to the Chicken Bucket!", description=f"{member.mention} joined! Say hi in {general}, won't you?", color=0xFFDF00)
  embed.set_image(url="https://media.tenor.com/images/50753729a279f8e68d9b6186fa12750b/tenor.gif")
  embed.set_footer(text="Regards from the bucket.", icon_url="https://giphy.com/gifs/wave-chicken-waving-u2Zl6MxdEsHp6")
  channel = discord.utils.get(bot.get_all_channels(), name="welcome-goodbye")
  await channel.send(embed=embed)
  #await channel.send(member.mention + " joined! Say hi, won't you?")
  role = discord.utils.get(member.guild.roles, name="hatchling")
  await member.add_role(role)
  role = discord.utils.get(member.guild.roles, name="wingman")
  await member.add_role(role)
@bot.event
async def on_member_remove(member):
  print(f"{member.mention} left...")
  channel = discord.utils.get(bot.get_all_channels(), name="welcome-goodbye")
  await channel.send(member.mention + " left... <:gurasit:764536034930982963>")

#who deleted message?
@bot.event
async def on_message_edit(before, after):
  if before.content == after.content:
    pass
  else:
    #print(before/after) to get properties
    print(f"{str(before.author)} edited a message saying \"{str(before.content)}\" to say \"{str(after.content)}\" in #{before.channel.name} in {before.guild}")
    esniped.append(before.content)
    esnipe_change.append(after.content)
    esnipeauthor.append(before.author)
@bot.event
async def on_message_delete(message):
  print("Message saying \"" + message.content + "\" from " + str(message.author) + " was deleted in #" + message.channel.name)
  sniped.append(message.content)
  snipeauthor.append(message.author)
@bot.event
async def on_message(message):
  if (not message.attachments) and message.author != bot.user and len(message.content) > 0:
    if message.content[0] == "-":
      await bot.process_commands(message)
    else:
      if "<@!735184223731712104>" in message.content:
        await message.channel.send("<:pinkguyping:773986025302130748>")
      if "yep" == message.content.lower():
        await message.channel.send("COCK")
      """if "hey" in message.content.lower().split():
        if "rawr x3 nuzzles!" in message.content.lower():
          pass
        else:
          await message.add_reaction("🇭")
          await message.add_reaction("🇪")
          await message.add_reaction("🇾")
          await message.add_reaction("🇲")
          await message.add_reaction("🇴")
          await message.add_reaction("🅾️")
          await message.add_reaction("🇳")
          await message.add_reaction("🇦")
          #await message.add_reaction("↗️")
          #await message.add_reaction("↘️")
          #await message.channel.send("HEY MOONA")"""
      if "gn" == message.content.lower():
        await message.channel.send("Sweet dreams bby ❤")
      if "gm" == message.content.lower():
        await message.channel.send("Good morning bby ❤")
        await message.channel.send(file=discord.File("files/guralarm.mp3"))
      if "what is padoru" in message.content.lower():
        await message.channel.send("""**What is Padoru?**\n\nPadoru isn't a word you would find in the English language, or any other language for that matter, to understand what Padoru means, first we need to talk about 'onomatopoeia', what does this big 6 syllable word mean? Onomatopoeia is the imitation of sound using language. For example when you're trying to describe a scene from your favourite superhero movie to your freind who has never seen it, you would be onomatopoeia to mimic the sound effects heard during that scene like and explosion, or the sound of a lazer beam being fired. What's important to note is that onomatopoeia has different varieties throughout various languages. We use onomatopoeia to describe the sound of a heart beating as "lub-dub", but in the japanese language, it is "doki-doki". Padoru is a Japanese onomatopoeia of the sound a reindeer makes when its hooves are clopping on the ground while they are running, and in the context of Christmas, the sounds of reindeer running and making the clopping sounds are heard worldwide on Christmas day when Santa delivers presents with his reindeer. Hence, Padoru and Christmas Day can be used interchangeably.""")

      if gameon == True and message.channel.id == 785758272778272798:
        #global gameon, guesses, guessed, used, wrong, indez, anime, updatemessage, response
        global guesses, guessed
        if message.content.lower() == anime.lower():
          guesses += 1
          await message.channel.send(f"Nice you got it. That took you {guesses} guesses to complete.")
          guessed = [True]
          checkCompletion()
        elif len(message.content) == 1 and message.content.lower() in letters:
          hangCheckLetter(message.content)
          await message.channel.send(response)
          await message.channel.send(hangUpdate())
          if wrong >= 6:
            await message.channel.send("You lose!")
            await message.channel.send(f"The anime was \"{anime}.\"")
            guessed = [True]
            checkCompletion()
          if checkCompletion():
            await message.channel.send(f"You took {guesses} guesses to complete!")

#how to get last argument in command - take all words written after command/params, split and save to list, iterate backwards
#guralarm, dan's guralarm, gay tea

"""@bot.event ##https://cdn.discordapp.com/attachments/381965515721146390/773265434853376020/unknown.png
async def on_command_error(ctx, error):
  print(f"{ctx.message.author} tried doing something that didn't exist...")
  #traceback.print_exception(type(error), error, error.__traceback__)
  if isinstance(error, commands.errors.MissingPermissions):
    await ctx.send("You can't do that mate.") #check what permissions needed?
    print("Missing Perms")
  elif isinstance(error, commands.errors.CommandNotFound):
    #await ctx.send("Not a command bruh.")
    print("Not a command")
  elif isinstance(error, commands.errors.MissingRequiredArgument):
    await ctx.send("You forgot to add args.")
    print("Missing args")
  elif isinstance(error, commands.errors.BadArgument):
    await ctx.send("You can't use that as a arg ¯\_(ツ)_/¯")
    print("Bad args")
separate error handlers for each command
"""
#on event mention

@bot.command(name="hangman")
async def hangman(ctx):
  global gameon, guesses, guessed, used, wrong, anime, updatemessage
  if gameon == False and ctx.channel.id == 785758272778272798:
    await ctx.send("Hangman game starting...")
    stuff = []
    with open("hangmananimeenglish.txt", "r") as file:
      for anime in file.readlines():
        stuff.append(anime[:-1])
    gameon = True
    guesses = 0
    wrong = 0
    guessed = []
    used = []
    anime = stuff[random.randint(0, len(stuff)-1)]
    for i in range(len(anime)):
      if anime[i] == " ":
        guessed.append(True)
      else:
        guessed.append(False)
    print(guessed)
    hangUpdate()
    await ctx.send(updatemessage)
  elif gameon == True and ctx.channel.id == 785758272778272798:
    await ctx.send("Hangman game already underway...")
@bot.command(name="hangend")
async def hangend(ctx):
  global gameon
  gameon = False
  await ctx.send("Hangman game has been ended.")

"""@bot.command(name="playgura")
async def playgura(ctx):
  user=ctx.message.author
  #print(user.voice)
  #print(user.voice.channel)
  if user.voice != None:
    voice_channel = user.voice.channel
    print(voice_channel)
    print(f"Binding to {voice_channel.name} to play gura for {ctx.message.author}.")
    
    #vc = await bot.join_voice_channel(voice_channel)
    vc = await bot.join_voice_channel(voice_channel)
    vc.play(source="files/guralarm.mp3")
    await asyncio.sleep(10)
    player = vc.create_ffmpeg_player('files/guralarm.mp3', after=lambda: print('done'))
    player.start()
    while not player.is_done():
        await asyncio.sleep(1)
    player.stop()
    await vc.disconnect()
  else:
    await ctx.send("Join a voice channel to use this command.")
https://stackoverflow.com/questions/53604339/how-do-i-make-my-discord-py-bot-play-mp3-in-voice-channel
"""
#sending image testing

#help command change - "already existing command" (check)
#different message for admin/members (check roles)
#change -help to embed (different help for admin/normies (check channel so normies don't see?))
#https://stackoverflow.com/questions/49751913/discord-py-bot-that-creates-a-role-with-permissions-how-to-do

#-clearcolors (reaction instead)
#suggestions - learn sql for database stuff, minesweeper, specific error message by command

#custom color roles, create_role with color https://discordpy.readthedocs.io/en/latest/api.html#discord.Guild.create_role
#revamp help command, double check tasks.loop by making a new one, change admin commands to check for perms, role commands for different stuff, organize commands (different files?)
#role react assingment


#https://www.programcreek.com/python/example/127968/discord.ext.tasks.loop


#log all commands/num commands (database?)
#troll / deping (mass ping, every 15 pings deletes channel and creates new one or dms??), args number of pings?
#chest/daily gift things (coins?)
#admin commands check perms instead of roles

#toggle on and off hey/horny/commands
#girl confirm remove background? ( change name to girlyes/girlyesbloody and change -yes command list)
#delete message by id?
#num commands (store in db?)(by guild and/or total)
#server stats
#creating new roles, setting color using input

#gif commands
#laugh - gilgamesh laughing gif (embed??)

#yes, sayemoji, coinflip shortened version where?
@bot.command(name="help")
async def help(ctx):
  embed=discord.Embed(title=f"Commands for the M-F Chicken", description="Prefix: -", color = discord.Colour.orange())
  if ctx.author.guild_permissions.administrator:
    embed.add_field(name="Admin Commands", value="mention, purge, clearsnipe, clearesnipe", inline=False)
  embed.add_field(name="Emojis", value="sayemoji, bersercar, blush, bruhping, humu, reverse, thonk, yes", inline=True)
  embed.add_field(name="Random", value="coinflip, diceroll, pickint, pickdec", inline=True)
  embed.add_field(name="Experimental", value="Under construction...", inline=True)
  embed.add_field(name="Misc", value="Under construction...", inline=True)
  embed.add_field(name="Weeb", value="gura, myanimelist (not working!), padoru, padorucountdown, sauce", inline=True)
  embed.add_field(name="Time", value="Under construction...", inline=True)
  #embed.add_field(name="Economy", value="Under construction...", inline=False)
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/735184223731712104/3591e49c765cd1a5ccfff8966097aacf.webp?size=1024")
  embed.set_footer(text="Regards from the bucket.", icon_url="https://cdn.discordapp.com/attachments/742258921733095437/770523030484156456/CHKN_BUCKET.png")
  await ctx.send(embed=embed)

class admin(commands.Cog, name="Admin-only"):
  #change like https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.has_any_role
  @commands.command(name="mention")
  async def owner(self, ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="CHKN")
    if role in ctx.author.roles:
      await ctx.send(member.mention)
    else:
      await ctx.send("You can't do that m8")
  @commands.command(name="purge")
  async def purge(self, ctx, num_messages: int = 2):
    role = discord.utils.find(lambda r: r.name == 'HEAD COCK', ctx.guild.roles)
    chkn = discord.utils.find(lambda r: r.name == "CHKN", ctx.guild.roles)
    if role in ctx.author.roles or chkn in ctx.author.roles:
      if chkn in ctx.author.roles or num_messages < 100:
        await ctx.channel.purge(limit=num_messages)
        print(str(num_messages) + " messages have been purged in #" + str(ctx.channel) + " by " + str(ctx.author))
      else:
        await ctx.send("Slow down there bud, don't get ahead of yourself.")
        print(str(ctx.author) + " tried to purge " + str(num_messages-100) + "more messages than they should.")
    else:
      await ctx.send("Normies can't do that.")
      print(str(ctx.author) + " the normie tried to purge messages")
  @commands.command(name="clearsnipe")
  async def clearsnipe(self, ctx):
    global sniped, snipedauthor
    sniped, snipedauthor = [], []
    role = discord.utils.get(ctx.guild.roles, name="CHKN")
    if role in ctx.author.roles:
      await ctx.send("Sniped logs have been cleared")
    else:
      await ctx.send("Normies can't do that.")
  @commands.command(name="clearesnipe")
  async def clearesnipe(self, ctx):
    global esniped, esniped_change, esnipedauthor
    esniped, esniped_change, esnipedauthor = [], [], []
    role = discord.utils.get(ctx.guild.roles, name="CHKN")
    if role in ctx.author.roles:
      await ctx.send("Esnipe logs have been cleared")
    else:
      await ctx.send("Normies can't do that.")
bot.add_cog(admin(bot))
class emojis(commands.Cog, name="Emojis"):
  """@commands.command(name="findemoji")
  async def findemoji(self, ctx, emojiname: str):
    emoji = discord.utils.get(ctx.guild.emojis, name=emojiname)
    if emoji != None:
      await ctx.send(emoji)
    else:
      await ctx.send(f"Could not find an emoji with the name {emojiname}.")"""
  @commands.command(name="sayemoji", aliases=["saye"])
  async def sayemoji(self, ctx, emojiname=None):
    emoji = discord.utils.get(ctx.guild.emojis, name=emojiname) #check all of guild bot is in?
    if emoji != None:
      await ctx.message.delete()
      await ctx.send(emoji)
    elif emojiname != None:
      await ctx.send(f"Could not find an emoji with the name {emojiname}.")
    else:
      await ctx.send("What emoji???")
  @commands.command(name="thonk")
  async def thonk(self, ctx):
    await ctx.message.delete()
    await ctx.send("<:moonacingthonk:775585700677681213>")
  @commands.command(name="reverse")
  async def reverse(self, ctx):
    await ctx.message.delete()
    await ctx.send("<:gurareverse:764536029813276672>")
  @commands.command(name="kazuya")
  async def kazuya(self, ctx):
    await ctx.message.delete()
    await ctx.send("<a:kazuya:757296201698902026>")
  @commands.command(name="humu")
  async def humu(self, ctx):
    await ctx.message.delete()
    await ctx.send("<:inahumu:770094814188142602>")
  @commands.command(name="blush")
  async def blush(self, ctx):
    await ctx.message.delete()
    await ctx.send("<:gurablush:764536032129187900>")
  @commands.command(name="yes")
  async def yes(self, ctx, tosend: int=None):
    yeslist = ["<:minetayep:764518299400667138>", "<:girlconfirmbloody:764518235441070130>", "<:girlconfirm:773779645107011634>"]
    if tosend == 1:
      await ctx.send(yeslist[0])
    elif tosend == 2:
      await ctx.send(yeslist[1])
    elif tosend == 3:
      await ctx.send(yeslist[2])
    else:
      tosend = random.randint(0, 2)
      await ctx.send(yeslist[tosend])
    await ctx.message.delete()
  @commands.command(name="bruhping")
  async def bruhping(self, ctx):
    await ctx.message.delete()
    await ctx.send("<:pinkguyping:773986025302130748>")
  @commands.command(name="bersercar")
  async def bersercar(self, ctx):
    await ctx.message.delete()
    await ctx.send("<:bersercar:774889361862557727>")
  #dorime - korone, calliope
  #gifs too (like that one bot in megumin discord)
bot.add_cog(emojis(bot))
class rangen(commands.Cog, name="Random"):
  #Flips coin, set number of coins is optional
  @commands.command(name="coinflip", aliases=["flipcoin", "fc", "cf"])
  async def coinflip(self, ctx, num_coins: int=1):
    tails=0
    heads=0
    if num_coins > 1000000:
      await ctx.send("Too many coins. 1 million max.")
    elif num_coins == 1:
      flip = random.randint(0, 1)
      print(flip)
      if flip == 0:
        await ctx.send("Tails")
      else:
        await ctx.send("Heads")
    else:
      coinedit = await ctx.send("Flipping coins :coin:")
      for i in range(num_coins):
        flip = random.randint(0, 1)
        if flip == 0:
          tails += 1
        else:
          heads += 1
      await coinedit.edit(content=f"Total heads: {heads} \nTotal tails: {tails}")
      print(f"In {num_coins} coinflips, there were {heads} heads and {tails} tails.")
  @coinflip.error
  async def coinflip_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send("That's not a flippable amount of coins.")
  #rolls x dice with y sides
  @commands.command(name="diceroll", help="Format: -diceroll _x_ _s_. \nRolls _x_ dice each with _s_ sides")
  async def diceroll(self, ctx, num_of_dice: int, num_of_sides: int):
    dicerolls = [
      str(random.choice(range(1, num_of_sides + 1)))
      for _ in range(num_of_dice) 
    ]
    await ctx.send(", ".join(dicerolls))
  #random number between x and y
  @commands.command(name="pickint")
  async def picknum(self, ctx, min_amount: int, max_amount: int):
    if min_amount > max_amount:
      min_amount, max_amount = max_amount, min_amount
      await ctx.send(random.randint(min_amount, max_amount))
    elif min_amount == max_amount:
      await ctx.send("That's the same number")
    else:
      await ctx.send(random.randint(min_amount, max_amount))
  @commands.command(name="pickdec")
  async def pickdec(self, ctx, min_amount: int=0, max_amount: int=1, rounding: int=None):
    randomnum = random.uniform(min_amount, max_amount)
    if min_amount == max_amount:
      await ctx.send("That's the same number")
    else:
      if rounding != None:
        await ctx.send(round(randomnum, rounding))
      else:
        await ctx.send(randomnum)
      #add rounding feature, default = None, else no rounding


bot.add_cog(rangen(bot))
class experimental(commands.Cog, name="Experimental"):
  #attempts to ping @everyone
  @commands.command(name="everyone")
  async def everyone(self, ctx):
    await ctx.send("@everyone")

  #attempts to ping @here
  @commands.command(name="here")
  async def here(self, ctx):
    await ctx.send("@here")

  @commands.command(name="linkers", help="NOT WORKING IDK yet, learning how to embed stuff")
  #USELESS testing embed
  async def linkers(self, ctx):
    await ctx.send("This command is under construction pls come back another time.")
    #await ctx.send("https://rauf.wtf/embed/yeeeet")

  @commands.command(name="testdm", help="NOT WORKING Testing if this bot can send/create dms.")
  #USELESS testing creating dm:
  async def testdm(self, ctx):
    print("Someone trying to test dm")
    await ctx.send("This command is under construction pls come back another time.")

  #testing purging messages (delete instead of purge?)
  @commands.command(name="deletethis", help="")
  async def deletethis(self, ctx):
    await ctx.message.delete()
    """messageid = ctx.message.id
    print(messageid)
    await delete_message(ctx)
    print(str(ctx.author) + " wants to delete themself")"""
    await ctx.send("You asked for it <:inahumu:770094814188142602>")
    print(str(ctx.author) + " deleted themself.")
  #tseting deleting own message

  @commands.command(name="deleteself", help="")
  async def deleteself(self, ctx):
    todelete = await ctx.send("I can do it like this if you want")
    await ctx.send("Or like this uwu", delete_after=6)
    await asyncio.sleep(4)
    await todelete.delete()
  #testing editing own message
  @commands.command(name="edithis", help="Edits message")
  async def edithis(self, ctx):
    message = await ctx.send("As you wish")
    await asyncio.sleep(1)
    await message.edit(content="Master")
  @commands.command(name="welcomeforcesend")
  async def welcomeforcesend(self, ctx):
    channel = discord.utils.get(bot.get_all_channels(), name="welcome-goodbye")
    #print(bot.get_all_channels())
    print(channel)
    await channel.send(f"are ya happy now {ctx.author.mention}")
  @commands.command(name="removethis")
  async def removethis(self, ctx):
    await ctx.message.delete()
    await ctx.send("did that work?")
  @commands.command(name="webhooktest")
  async def webhooktest(self, ctx):
    await ctx.send("This command is under construction pls come back another time. (potentially never coming back")
  @commands.command(name="embedtest")
  async def embedtest(self, ctx):
    embed = discord.Embed(title="Title is Title", description="What more needs to be said", color=0xF46216)
    #discord.Colour.___? or Colour.___? check with https://www.htmlcsscolor.com/
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/274036740149215232/ab773e6f8426d1feec26d31bd9f84b55.jpg?size=1024')
    embed.set_image(url="https://media1.tenor.com/images/c00ff77b181a298ad1cbcee2977283e8/tenor.gif")
    embed.add_field(name="<a:padoruspin:775586265026265129>", value="IDK what i'm doing here", inline=False)
    embed.add_field(name="Field2", value="Or here but it's ", inline=True)
    embed.add_field(name="Field3", value="supposed to be inline and a link [here](https://www.youtube.com/)...", inline=True)
    embed.add_field(name="Field4", value="Let's see how many inlines i can get", inline=True)
    embed.add_field(name="Field5", value="Hope it's still inline heh", inline=True)
    embed.set_author(name="Multi-Feathered Chicken", icon_url="https://cdn.discordapp.com/attachments/742258921733095437/775061627695005736/bersercar.jpg")
    embed.set_footer(text="Regards from the bucket.", icon_url="https://cdn.discordapp.com/attachments/742258921733095437/770523030484156456/CHKN_BUCKET.png")
    await ctx.send(embed=embed)
  @commands.command(name="embedinput")
  async def embedinput(self, ctx, *, given: str="IDK man..."):
    await ctx.message.delete()
    embed = discord.Embed(
      title="",
      description="",
      color=discord.Colour.blue())
    embed.add_field(name="\u200b", value=f"{given}", inline=False)
    #https://github.com/Rapptz/discord.py/issues/643
    embed.set_footer(text="Regards from the bucket.", icon_url="https://cdn.discordapp.com/attachments/742258921733095437/770523030484156456/CHKN_BUCKET.png")
    await ctx.send(embed=embed)
  @commands.command(name="embedimg")
  async def embedimg(self, ctx, link: str):
    await ctx.message.delete()
    embed=discord.Embed(
      title="",
      description="",
      color=discord.Colour.blue())
    embed.set_image(url=link)
    embed.set_footer(text="Regards from the bucket.", icon_url="https://cdn.discordapp.com/attachments/742258921733095437/770523030484156456/CHKN_BUCKET.png")
    await ctx.send(embed=embed)
    #role assignment
  @commands.command(name="pekome")
  async def pekome(self, ctx):
    role = discord.utils.get(ctx.guild.roles, name="useless-peko")
    print(role)
    if role in ctx.author.roles:
      await ctx.send("You alread have the role!")
    else:
      await ctx.author.add_roles(role)
      await ctx.send("You have been peko'd.")
  @commands.command(name="unpeko")
  async def unpeko(self, ctx):
    role = discord.utils.get(ctx.guild.roles, name="useless-peko")
    if role in ctx.author.roles:
      await ctx.author.remove_roles(role)
      await ctx.send("You've been un-peko'd... why... ")
    else:
      await ctx.send("You aren't peko'd...")
  #mention someone and give role to them (try doing this with mute later?)
bot.add_cog(experimental(bot))
class misc(commands.Cog, name="Misc"):
  #API latency????
  @commands.command(name="ping")
  async def ping(self, ctx):
    await ctx.send(f"API Latency is {round(bot.latency * 1000)}ms or something like that")
  #responds, just for checking if bot is up
  @commands.command(name="test")
  async def test(self, ctx):
    await ctx.send("I just want to sleep pls")
  #repeats what is said after command
  @commands.command(name="say", help="Bot repeats text following command one word at a time. \nMultiple words can be sent with one text by adding double quotes around them. This also allows for -say to repeat multiple lines as they are sent.")
  async def say(self, ctx, *, args):
    await ctx.message.delete()
    print(str(ctx.author) + " wants to say " + args + ". Like bruh...")
    await ctx.send(args)
  @commands.command(name="snipe")
  async def snipe(self, ctx, index: int=1):
    if not (index > len(sniped)):
      tosnipe = index * -1
      await ctx.send(f"{sniped[tosnipe]}\n- {snipeauthor[tosnipe]}")
    else:
      await ctx.send("Haven't logged that many deletes mate ¯\_(ツ)_/¯")
  @commands.command(name="esnipe")
  async def esnipe(self, ctx, index: int=1):
    if not (index > len(esniped)):
      toesnipe = index * -1
      await ctx.send(f"\"{esniped[toesnipe]}\" was changed to say \"{esnipe_change[toesnipe]}\"\n- {esnipeauthor[toesnipe]}")
    else:
      await ctx.send("Haven't logged that many edits mate ¯\_(ツ)_/¯")
  @commands.command(name="avatar", aliases=["av"])
  async def avatar(self, ctx, *, member: discord.Member = None):
    if member == None:
      await ctx.send(ctx.author)
      await ctx.send(ctx.author.avatar_url)
    else:
      await ctx.send(member)
      await ctx.send(member.avatar_url)
  @commands.command(name="membercount", aliases = ["mc"])
  async def membercount(self, ctx):
    global guild
    await ctx.send(f"Member Count: {guild.member_count}")
  @commands.command(name="horny", help="Sends randomized message(or image).")
  async def horny(self, ctx):
    horny_response = ["Bonk", "Not here", "Horny jail", "Stop that", "***no***", "No please no", "How lewd", "Not **that** word"]
    await ctx.send(random.choice(horny_response))
  @commands.command(name="rawr")
  async def rawr(self, ctx):
    await ctx.message.delete()
    await ctx.send("rawr x3 nuzzles! pounces on u, uwu u so warm. couldn't help but notice ur bulge from across the floor, nuzzlez yo' necky~ murr~ hehe unzips yo baggy ass pants, oof baby u so musky take me home, pet me, N' make me yours & dont forget to stuff me! see me wag my widdle baby tail, all for your bolgy-wolgy! kisses n lickies yo neck, i hope daddy likeies nuzzles n wuzzles yo chest, i be gettin thirsty hey i got a lil itch, u think u can help me? only seven inches long uwu PLS ADOPT ME paws on ur bulge as i lick my lips (uwu punish me pls) bout hit'em with this furry shit (he don't see it com")
bot.add_cog(misc(bot))
class weebstuff(commands.Cog, name="Weeb"):
  @commands.command(name="gura")
  async def gura(self, ctx):
    await ctx.message.delete()
    await ctx.send("Guys, I'm shaking. I'm fucking shaking. I've never wanted to breed with anyone more than I want to with Gawr Gura. That perfect, loli body. Those flat hydrodynamic breasts. The child bearing hips of a literal goddess. It honestly fucking hurts knowing that I'll never mate with her, pass my genes through her, and have birth a set of perfect baby shark humans. I'd do FUCKING anything for the chance to get Gawr Gura pregnant. A N Y T H I N G. And the fact that I can't is quite honestly too much fucking bear. Why would Yagoo create something so perfect? To fucking tantalize us? Fucking laugh in our faces?! Honestly guys I just fucking can't anymore. Fuck. <:gurablush:764536032129187900>")
  @commands.command(name="padoru", help="padoru")
  async def padoru(self, ctx):
    print(str(ctx.author) + " says it's Christmas.")
    #add field instead of messages?
    await ctx.send("HASHIRE SORI YO")
    await asyncio.sleep(2)
    await ctx.send("KAZE NO YOU NI")
    await asyncio.sleep(2)
    await ctx.send("TSUKIMIHARA WO")
    await asyncio.sleep(2.2)
    await ctx.send("***__PADORU PADORU__***")
    await asyncio.sleep(2)
    await ctx.send("<a:padoruspin:775586265026265129>MERRY CHRISTMAS EVERYONE!<a:padoruspin:775586265026265129>")
    await asyncio.sleep(1.5)
    await ctx.send("https://tenor.com/view/padoru-padoru-anime-run-fate-series-saber-nero-gif-15979862")
    #edit message to add one word at a time?
  @commands.command(name="padorucountdown", aliases=["pcd", "padorucd"]) #https://repl.it/@RyanLee35/Padoru-Countdown-datetime-testing#main.py
  async def padorucountdown(self, ctx):
    today = timezone.localize(datetime.now())
    delta = padoruday - today
    deltadays = delta.days
    catdeltahours = delta.seconds//3600
    catdeltaminutes = delta.seconds % 3600 // 60
    catdeltaseconds = delta.seconds % 3600 % 60
    await ctx.send(f"There are {deltadays} days, {catdeltahours} hours, {catdeltaminutes} minutes, and {catdeltaseconds} seconds until padoru.<a:padoruspin:775586265026265129> (at least in PDT. I'll find a way to adjust timezones later for you est fucks. and canadians. and asians.)")
  #@bot.command(name="mal/anime/manga") webscraping
  @commands.command(name="myanimelist", aliasese=["mal"])
  async def myanimelist(self, ctx):
    await ctx.send("This command is under construction pls come back another time.")
  #random number from 1-350000
  @commands.command(name="sauce", help="Picks a random number between 1 and 350000.")
  async def sauce(self, ctx):
    saucer = await ctx.send(random.randint(1, 350000))
    await asyncio.sleep(3)
    await saucer.edit(content=":wink:")#edit or delete?
bot.add_cog(weebstuff(bot))
class timestuff(commands.Cog, name="Time"):
  @commands.command(name="gmt")
  async def gmt(self, ctx):
    await ctx.send("""```Time zones:\nGMT-12 	-  International Date Line West (IDLW)\nGMT-11	 -  Nome Time (NT)\nGMT-10	 -  Hawaii Standard Time (HST)\nGMT-9	  -  Alaska Sandard Time (AKST)\nGMT-8	  -  Pacific Standard Time (PST)\nGMT-7  	-  Mountain Standard Time (MST)\nGMT-6  	-  Central Standard Time (CST)\nGMT-5  	-  Eastern Standard Time (EST)\nGMT-4  	-  Atlantic Standard Time (AST)\nGMT-3  	-  Argentina Time (ART)\nGMT-2	  -  Azores Time (AT)\nGMT-1	  -  West Africa Time (WAT)\nGMT+/-0    -  Greenwich Mean Time (GMT)\nGMT+1	  -  Central European Time (CET)\nGMT+2	  -  Eastern European Time (EET)\nGMT+3	  -  Moscow Time (MSK)\nGMT+4	  -  Armenia Time (AMT)\nGMT+5	  -  Pakistan Standard Time (PKT)\nGMT+6	  -  Omsk Time (OMSK)\nGMT+7	  -  Kranoyask Time (KRAT)\nGMT+8	  -  China Standard Time (CST)\nGMT+9	  -  Japan Standard Time (JST)\nGMT+10	 -  Eastern Australia Standard Time (AEST)\nGMT+11 	-  Sakhalin Time (SAKT)\nGMT+12 	-  New Zealand Standard Time (NZST)``` Same thing as UTC.""") #\nVisit [this link](https://greenwichmeantime.com/) for more help
  @commands.command(name="utc")
  async def utc(self, ctx):
    await ctx.send("""```Time zones:\nUTC-12 	-  International Date Line West (IDLW)\nUTC-11	 -  Nome Time (NT)\nUTC-10	 -  Hawaii Standard Time (HST)\nUTC-9	  -  Alaska Sandard Time (AKST)\nUTC-8	  -  Pacific Standard Time (PST)\nUTC-7  	-  Mountain Standard Time (MST)\nUTC-6  	-  Central Standard Time (CST)\nUTC-5  	-  Eastern Standard Time (EST)\nUTC-4  	-  Atlantic Standard Time (AST)\nUTC-3  	-  Argentina Time (ART)\nUTC-2	  -  Azores Time (AT)\nUTC-1	  -  West Africa Time (WAT)\nUTC+/-0    -  Greenwich Mean Time (UTC)\nUTC+1	  -  Central European Time (CET)\nUTC+2	  -  Eastern European Time (EET)\nUTC+3	  -  Moscow Time (MSK)\nUTC+4	  -  Armenia Time (AMT)\nUTC+5	  -  Pakistan Standard Time (PKT)\nUTC+6	  -  Omsk Time (OMSK)\nUTC+7	  -  Kranoyask Time (KRAT)\nUTC+8	  -  China Standard Time (CST)\nUTC+9	  -  Japan Standard Time (JST)\nUTC+10 	-  Eastern Australia Standard Time (AEST)\nUTC+11 	-  Sakhalin Time (SAKT)\nUTC+12 	-  New Zealand Standard Time (NZST)``` Same thing as GMT.""")
bot.add_cog(timestuff(bot))

class economy(commands.Cog, name="Economy"):
  @commands.command(name="daily")
  async def daily(self, ctx):
    pass
  @commands.command(name="bucket")
  async def bucket(self, ctx):
    pass
#bot.add_cog(economy(bot))
#daily only check message, no specific command? (send a message, if at least x time from last message reward, reward given + timer reset)

#indicating an image?/checking if is an acutal link?
"""
repes = 0
@tasks.loop(seconds=5.0)
async def looptest():
  global repes
  repes += 1
  channel = bot.get_channel(770422424495849474)
  await channel.send(f"This message #{repes} that occurs every 5 seconds.")
@looptest.before_loop
async def before():
  await bot.wait_until_ready()
looptest.start()"""
#looping messages https://stackoverflow.com/questions/57631314/making-a-bot-that-sends-messages-at-a-scheduled-date-with-discord-py

#sending images like emotes
#reddit, twitter webscrape? or youtube

"""@bot.command(name="gifthing")
async def gifthing(ctx, site, description):
  picker = random.choice(range(0, 2))
  if site.lower() == "tenor" or (site.lower() != "giphy" and picker == 0):
    await ctx.send("/tenor " + description)
  else:
    await ctx.send("/giphy " + description)"""


"""
#moving channel between categories?

@bot.command(name='create-channel')
@commands.has_role('____________')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


creating channel with specific role, error message if role not contained?(what if non  existent)
"""

"""
@tasks.loop(hours=24)
async def onceaday():
  channel = bot.get_channel(742258921733095437)
  #self.index += 1
  #print(self.index)
  await channel.send("Here's the daily message!")
@onceaday.before_loop
async def before():
  await bot.wait_until_ready()
  print("1 day have passed.")
onceaday.start()
"""

keep_alive.keep_alive()
bot.run(token, bot=True, reconnect=True)
#bot.run(token) what is differene, what is reconnect

#client code
"""#what does raising exception do
  elif message.content == "raise-exception":
    raise discord.DiscordException
#increment/counter for certain things
#https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#exception-hierarchy
"""

"""
things to do

create new channels/roles
auto assign roles on join, reaction roles(colors), role limited commands
mute role?

edit thonk emoji
add suggested emotes
get darrick to test join/leave messages (setting channel + sending there)

-disable commands?

how to take in multiple inputs (tea, chess coords)

games
game of Nim (misere or regular)
rpg/dungeon, chess
minesweeper

links (raf thingy, like plz megu looking thing)
plz megu thing (webscraping?)
images (dyno role images generated/created how?)
unprompted messages(pokemon spawn/halloween bot)
how to send images/custom emotes?
twitter/reddit feed
server stats
chains
i control bot how (send dms to matthew)
polls/poll channel
moderation stuff(mute, ban, kick, warn, etc)
create category/channels, game channels for specific person?
bot/mod logs
sending emotes/images
birthday countdown(by timezone?)
gn/gm message (sunshine gura)(gurasunshine + guraheart emoji)(kiryu coco good morning motherfuckers)
lists, avatars, set a profile

music/video - file, youtube, spotify, etc?
chatbot/question
can bot say any emoji if in server + have name/id for emoji? (gif emojis too?)
anime gifs (love is war)
jojo (rero)
dorime/padoru emotes
creating images(level cards)
on event (certain reactions?)
list/todo
search command
mal search like tcs/scss (webscraping?)
korone the ripper emoji
member count
orbital fill
BIRTHDAY THING
scatman - scattydobodobodibibibiodbi

adding suffixes to commands??? (or osmething like mudae flags)

@client.command()
async def nickchange(ctx, member: discord.Member, *, nick):
  await member.edit(nick=nick)

"""
"""
MANAGE ROLES

levels - sql?
make a database for levels? total commands?
(guilds + channels bot is int)
levels/xp (by guild, cumulative?)
timezone, personal profile? (transferrable)

what is hosting for if i just run and leave it

how to use resources in discord portal (javascript?)


different commands by server?
@bot.check
async def bot_check(ctx):
    # return True if command is enabled
    # raise commands.DisabledCommand if its disabled
    # Catch DisabledCommand in your error handler
    # Do whatever you want when command disabed in the error handler
"""
#await send(content=None, *, tts=False, embed=None, file=None, files=None, delete_after=None, nonce=None, allowed_mentions=None)
#await fetch_message(id)
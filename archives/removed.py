#give self color role + removing all color roles
@bot.command(name="colorme")
async def colorme(ctx, *, code):
  totalroles = 0
  for role in ctx.message.author.guild.roles:
    totalroles += 1
  codes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
  code = code.upper()
  for role in ctx.message.author.roles:
    print(role)
    if "Color Role" == role.name: #not workign?
      await ctx.message.author.remove_roles(role)
      await role.delete()
  if len(code) == 6:
    allin = True
    for i in code:
      if i in codes:
        pass
      else:
        allin = False
    if allin == False:
      await ctx.send("That's not a proper color code.")
    else:
      color = "0x" + code
      color = int(color, 16)
      guild = ctx.guild
      role = await guild.create_role(name="Color Role", colour=discord.Colour(color))
      await role.edit(position=totalroles-3)
      #https://stackoverflow.com/questions/58975932/changing-role-hierarchy-with-discord-py
      #https://stackoverflow.com/questions/48216914/how-to-add-and-create-roles-in-discord-py
      #color hex convert - https://stackoverflow.com/questions/21669374/convert-string-to-hex-in-python/21669393
        #check if user already has color roles, remove/delete role is exists and replace
      await ctx.message.author.add_roles(role)
  else:
    await ctx.send("That's not a proper color code.")
@bot.command(name="clearcolor")
async def clearcolor(ctx):
  for role in ctx.message.author.guild.roles:
    if role.name == "Color Role":
      await role.delete()
      removed += 1
  await ctx.send(f"{removed} color roles have been delete.")

#check if hangman game in progress
@bot.command(name="hangcheck")
async def hangcheck(ctx):
  if anime != "":
    await ctx.send(anime)
  else:
    await ctx.send("Start a game first.")

#send message to dan test server
@bot.command(name="hidan")
async def hidan(ctx):
  guild = discord.utils.get(bot.guilds, name="Test Server")
  print(guild)
  channel = discord.utils.get(guild.channels, name="test")
  print(channel)
  await channel.send("Hey dan")
  await ctx.send('heh')

#padoru emoji dm spam
@bot.command(name="trollme")
async def trollme(ctx, member: discord.Member):
  await ctx.send("<a:padoruspin:775586265026265129>")
  for i in range(10):
    await member.send("<a:padoruspin:775586265026265129>")
    await asyncio.sleep(0.5)

#webhook thing
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url("https://discordapp.com/api/webhooks/774519149031587861/nnKtLPKXpVWCBznbahR47VGwyHGFCaaoP1VzZlmhYzRcKVbDz7hXY1n6tR3h13Wldkxq", adapter=AsyncWebhookAdapter(session))
        await webhook.send('Hello World', username='Foo')

https://docs.aiohttp.org/en/stable/index.html

#padoru countdown and updatepadoru
@bot.command(name="updatepadoru")
async def updatepadrou(ctx):
  global daychecker, daydifference
  edited = False

  channel = bot.get_channel(777255472641736705)
  message = channel.fetch_message(791739951859499089)

  timenow = timezone.localize(datetime.now())
  untill = padoruday - timenow
  daystill = untill.days
  hourstill = untill.seconds//3600
  minutestill = (untill.seconds-hourstill*3600)//60
  secondstill = untill.seconds-((hourstill*3600) + (minutestill*60))

  if daystill >= 1:
    await channel.send(content=f"There are still {daystill} days, {hourstill} hours, and {minutestill} minutes until padoru.")
    edited = True
    daychecker = False
  #makes sure not to start this if message already sent for day, only works if less than a day to padoru
  elif daystill < 1:
    if hourstill > 1:
      await message.edit(content=f"There are {hourstill} hours, {minutestill} minutes, and {secondstill} until padoru.")
      edited = True
    elif minutestill > 1:
      await message.edit(content=f"There are {minutestill} minutes and {secondstill} seconds until padoru.")
      edited = True
    elif secondstill > 1:
      await message.edit(content=f"{secondstill} seconds until padoru.")
      edited = True
    else:
      await channel.send("HASHIRE SORI YO")
      await asyncio.sleep(2)
      await channel.send("KAZE NO YOU NI")
      await asyncio.sleep(2)
      await channel.send("TSUKIMIHARA WO")
      await asyncio.sleep(2.2)
      await channel.send("***__PADORU PADORU__***")
      await asyncio.sleep(2)
      await channel.send("MERRY CHRISTMAS EVERYONE!")
      await asyncio.sleep(1.5)
      await channel.send("https://tenor.com/view/padoru-padoru-anime-run-fate-series-saber-nero-gif-15979862")
      await channel.send("<a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129>")

  if edited = True:
    await ctx.send("Padoru counter has been updated! Go check it out in #padoru-counter")

  if (daydifference-daystill) > 0:
    daychecker = True
    daydifference = daystill
  else:
    daychecker = False
#send message saying padoru has been updated and check channel(linked)

#loops taking variable seconds?
#print every hour, not every day?

imminence, imminencechecktwo, minutetime, hourtime, daychecker = True, True, False, False, True
lastsend, checkint = 0, 3600.0
daydifference = 6
#use txt file? for what?
@tasks.loop(seconds=300.0)
async def padorucheck():
  channel = bot.get_channel(777255472641736705)
  message = await channel.fetch_message(791739951859499089)

  global imminence, imminencechecktwo, daychecker, checkint, minutetime, hourtime, daydifference, lastsend
  
  timenow = timezone.localize(datetime.now())
  #print(f"{timenow} is sending padoru count on {padoruday}.")
  """
  if lastsend == 0:
    print(lastsend)
  else:
    print(timenow - lastsend)
  """
  untill = padoruday - timenow
  daystill = untill.days
  hourstill = untill.seconds//3600
  minutestill = (untill.seconds-hourstill*3600)//60
  secondstill = untill.seconds-((hourstill*3600) + (minutestill*60))

  #print(f"{daystill} days, {hourstill} hours, {minutestill} minutes and {secondstill} seconds.")
  
  #sends new message/changes message refresh rate when - there is less than 1 day/minute within an hour until padoru (true/false statements limit to occur once)
  if (minutestill <= 1) and (daystill < 1) and (minutetime == False):
    minutetime = True
    print("Stopping loop to adjust to 1 second")
    padorucheck.cancel()
  elif (hourstill <= 1) and (daystill < 1) and (hourtime == False):
    hourtime = True
    print("Stopping loop to adjust to 60 seconds")
    padorucheck.cancel()
  elif (daystill < 1) and (imminence == False) and imminencechecktwo == False:
    imminence = True
    imminencechecktwo = True
    await channel.send("<a:padoruspin:775586265026265129>Padoru is looming. Be prepared<a:padoruspin:775586265026265129>")
  #limits message refresh rate so only one message can be sent per day while there is more than 1 day until padoru
  if (daydifference-daystill) > 0:
    daychecker = True
    daydifference = daystill
  else:
    daychecker = False
  #checks if more than 1 day to padoru and message not send in the same day
  if daystill >= 1 and daychecker == True:
    await message.edit(content=f"There are still {daystill} days, {hourstill} hours, and {minutestill} minutes until padoru.")
    daychecker = False
  #makes sure not to start this if message already sent for day, only works if less than a day to padoru
  elif daystill < 1:
    if hourstill > 1:
      await message.edit(content=f"There are {hourstill} hours, {minutestill} minutes, and {secondstill} seconds until padoru.")
    elif minutestill > 1:
      await message.edit(content=f"There are {minutestill} minutes and {secondstill} seconds until padoru.")
    elif secondstill > 1:
      await message.edit(content=f"{secondstill} seconds until padoru.")
    else:
      #doesn't work
      await channel.send("HASHIRE SORI YO")
      await asyncio.sleep(2)
      await channel.send("KAZE NO YOU NI")
      await asyncio.sleep(2)
      await channel.send("TSUKIMIHARA WO")
      await asyncio.sleep(2.2)
      await channel.send("***__PADORU PADORU__***")
      await asyncio.sleep(2)
      await channel.send("MERRY CHRISTMAS EVERYONE!")
      await asyncio.sleep(1.5)
      await channel.send("https://tenor.com/view/padoru-padoru-anime-run-fate-series-saber-nero-gif-15979862")
      await channel.send("<a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129><a:padoruspin:775586265026265129>")
      padorucheck.stop()
  #lastsend = timenow
@padorucheck.before_loop
async def before():
  await bot.wait_until_ready()
@padorucheck.after_loop
async def after():
  global minutetime, hourtime
  #interval not changed, doesn't start loop?
  if minutetime == True:
    change_interval(seconds=1.0)
    await channel.send("<a:padoruspin:775586265026265129>Padoru is imminent.<a:padoruspin:775586265026265129>")
    print("Padoru interval adjusted to 1 second.")
    padorucheck.start()
  elif hourtime == True:
    change_interval(seconds=60.0)
    await channel.send("<a:padoruspin:775586265026265129>Padoru is approaching. <a:padoruspin:775586265026265129>")
    print("Padoru interval adjusted to 60 seconds.")
    padorucheck.start()
  else:
    channel = bot.get_channel(777255472641736705)
    await channel.send("Thank you for counting down to padoru with me!")
#starts loop
padorucheck.start()
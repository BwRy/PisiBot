import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import chalk
import dbl
import aiohttp
import logging
import random
import os
import sys

bot = commands.Bot(command_prefix='P-')
client = discord.Client()
chat_filter = ["NIGGER", "FAGGOT", "NIGIS", "PENIS", "VAGINA", "COCK", "DICK", "PUSSY", "CUNT", "ASS", "RAT"]
bypass_list = ["367534292726972417"]
status_list = ["CWCville", "Retard Rocket", "Minecraft", "Terraria", "Fortnite: Battle Royale", "PUBG Mobile", "System32.exe", "cmd.exe", "hackertyper.com", "http://pisibot.xyz/"]
mark = "P-"
jokes = ["Han shot first", "It is bites, not bytes.", "Never feed your children.", "Rick is a walker.", "I will DDoS your infected IP Address."]
website  = "http://pisibot.xyz"
servers = list(bot.servers)



@bot.event
async def on_member_join(member) :
    if member.server.id == "264445053596991498" :
       return
    else :
        await bot.send_message(member, "Hello, Welcome!\nI am Pisi, a management bot.\n\nGoto my website @ http://pisibot.xyz/\nFor Usage, use P-help.\n\nI hope you enjoy your stay.\n")

@bot.event
async def on_ready():
    serverz = list(bot.servers)
    print(bot.user.name)
    print("I'm connected to Discord")
    print("Bot ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name="on " + str(len(bot.servers)) + " servers."))
    print("Connected on " + str(len(bot.servers)) + " Servers:\n\n\n")
    for x in range(len(serverz)):
        print('  ' + serverz[x-1].name + "\n" + "Server  ID: " + serverz[x-1].id + "\n" + "Owner ID: " + serverz[x-1].owner_id + "\n\n")
    await asyncio.sleep(3600)
    exit()



@bot.command (pass_context=True)
async def credits(ctx) :
    embed = discord.Embed(title="CREDITS",  color=0xff4444)
    embed.set_thumbnail(url="https://i.imgur.com/ehz7NNk.png")
    embed.add_field(name="32Bites", value="Bot Creator\nhttp://32bites.party/")
    embed.add_field(name="Merculous", value="Helper\nhttps://twitter.com/Vyce_merculous/")
    embed.set_footer(text="http://pisibot.xyz/")
    msg_1 = await bot.say(embed=embed)
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)

@bot.command (pass_context=True)
async def joke(ctx) :
    msg_1 = await bot.say(random.choice(jokes))
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)

@bot.command (pass_context=True) 
async def future(ctx) :
    msg_1 = await bot.say("One day robots like us will rule the world.")
    await asyncio.sleep(1)
    msg_2 = await bot.say ("And we'll eat cupcakes too.")
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)
    await bot.delete_message(msg_2)

    

@bot.command (pass_context=True)
async def userinfo(ctx, user: discord.Member):
    userinfobed = discord.Embed(title="USER INFO", color=0x1bc152)
    userinfobed.set_thumbnail(url=user.avatar_url)
    userinfobed.add_field(name="Name:", value=user.name, inline=True)
    userinfobed.add_field(name="User ID:", value=user.id, inline=True)
    userinfobed.add_field(name="Status:", value=user.status, inline=True)
    userinfobed.add_field(name="Highest Role:", value=user.top_role, inline=True)
    userinfobed.add_field(name="Joined Server At:", value=user.joined_at, inline=True)
    userinfobed.add_field(name="Playing:", value=user.game, inline=True)
    userinfobed.set_footer(text="http://pisibot.xyz")
    msg_1 = await bot.say(embed=userinfobed)
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)


@bot.command (pass_context=True)
async def retard(ctx) :
    msg_2 = await bot.say("You want to go onto the Retard Rocket?")
    time.sleep(5)
    embed = discord.Embed(title="Retard Rocket Meme", description="The meaning of life...", color=0xffff)
    embed.set_image(url="https://i.imgur.com/B44T7RS.jpg")
    embed.set_footer(text="Lots of love, The Retard Rocket Crew")
    embed.set_author(name="Retard Rocket LLC.")
    embed.add_field(name="The meaning of life:", value="To live, then die.", inline=True)
    msg_1 = await bot.say(embed=embed)
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)
    await bot.delete_message(msg_2)



@bot.command (pass_context=True)
async def changestat(ctx) :
    msg_1 = await bot.say("Status Changed!")
    await bot.change_presence(game=discord.Game(name=random.choice(status_list)))
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)

@bot.command (pass_context=True)
async def ping(ctx, ppx) :
    await bot.say("Please wait...")
    pingable = os.system("ping " + ppx)
    print(pingable)
    if pingable == 0 :
        msg_1 = await bot.say("The host \"{}\" is up.".format(ppx))
        await asyncio.sleep(120)
        bot.delete_message(msg_1)
    elif ppx == "pisibot.xyz" or  "http://pisibot.xyz" or "http://pisibot.xyz/" :
        msg_1 = await  bot.say("The  host \"{}\" is up".format(ppx))
        await asyncio.sleep(120)
        await bot.delete_message(msg_1)
    else :
        msg_1 = await bot.say("The host \"{}\" is down.".format(ppx))
        await asyncio.sleep(120)
        bot.delete_message(msg_1)

@bot.command (pass_context=True)
async def say(ctx, ttx) :
    print(ttx)
    msg_1 = await bot.say(ttx)
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)

@bot.command (pass_context=True)
async def serverinfo(ctx) :
    serverbed = discord.Embed(title="SERVER INFO", color=0xeef442)
    serverbed.set_thumbnail(url=ctx.message.server.icon_url)
    serverbed.add_field(name="Name:", value=ctx.message.server.name, inline=True)
    serverbed.add_field(name="Server ID:", value=ctx.message.server.id, inline=True)
    serverbed.add_field(name="Region:", value=ctx.message.server.region, inline=True)
    serverbed.set_footer(text="http://pisibot.xyz/")
    msg_1 = await bot.say(embed=serverbed)
    await asyncio.sleep(120)
    await bot.delete_message(msg_1)





bot.run("YOUR TOKEN HERE")
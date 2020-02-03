# cardreader @author Liam Hart

# HTTP Requests Stuff
import requests


# Hearthstone Information

# Single Card Info
url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards/'

def find_card_info(name):
    name = name.replace('-', '%20')
    global url
    cardURL = url + name
    r = requests.get(cardURL, headers={
    "X-Mashape-Key": <KEY>,
    "Accept": "application/json"
    })
    try:
        info = r.json()[0]
    except KeyError as e:
        
        return -1
    return info


# Discord API stuff
import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Turning gears...")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")

@bot.command(pass_context=True)
async def profile(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x4584b6)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Bye, {}.".format(user.name))
    await bot.kick(user)
    
# Code for translate command
@bot.command(pass_context=True)
async def translate(ctx, message):
    res = translate_text_english(message)
    embed = discord.Embed(title="Translating...", color=0x4584b6)
    lang = translate_client.detect_language(message)
    embed.add_field(name="From:",value=lang['language'],inline=True)
    embed.add_field(name="To:",value='en',inline=True)
    embed.add_field(name="Result",value=res,inline=True)
    await bot.say(embed=embed)

# Code for Hearthstone command(s)
@bot.command(pass_context=True)
async def dt(ctx, card_name):
    info = find_card_info(card_name)
    imgURL = 'https://drslash.com/wp-content/uploads/2014/07/Hearthstone.png'
    embed = discord.Embed(color=0x4584b6)
    embed.set_author(name="{}#{}".format(info['name'],info['cardId']),icon_url=imgURL)
    embed.add_field(name='Name',value=info['name'] if 'name' in info else 'None',inline=True)
    embed.add_field(name='Card Set',value=info['cardSet'] if 'cardSet' in info else 'None',inline=True)
    embed.add_field(name='Type',value=info['type'] if 'type' in info else 'None',inline=True)
    embed.add_field(name='Faction',value=info['faction'] if 'faction' in info else 'None',inline=True)
    embed.add_field(name='Rarity',value=info['rarity'] if 'rarity' in info else 'None',inline=True)
    embed.add_field(name='Cost',value=info['cost'] if 'cost' in info else 'None',inline=True)
    embed.add_field(name='Attack',value=info['attack'] if 'attack' in info else 'None',inline=True)
    embed.add_field(name='Health',value=info['health'] if 'health' in info else 'None',inline=True)
    embed.add_field(name='Effect',value=info['text'] if 'text' in info else 'None',inline=True)
    embed.add_field(name='About',value=info['flavor'] if 'flavor' in info else 'None',inline=True)
    embed.set_thumbnail(url=str(info['imgGold']))
    await bot.say(embed=embed)
    

    
bot.run("<API_KEY>")




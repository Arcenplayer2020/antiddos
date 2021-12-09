import random

import discord
import json
from  discord.ext import commands
import config
with open('blacklist.json','r') as file:
    black_listJson = json.load(file)
black_list = black_listJson
print(black_listJson)
print(type(black_list))
integers = {}


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = ';', intents=intents)
@bot.event
async def on_ready():
    print('Bot Connected')

@bot.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def bl(ctx,member):
    print(member)
    black_list.append(member)
    await ctx.send('пользователь забанен')
    with open('blacklist.json','w') as file:
        json.dump(black_list,file,indent=2,ensure_ascii=False)


    print(black_list)
@bot.event
async def on_member_join(member):
    print(str(member))
    if str(member) in black_list:
        await member.ban(reason='in bl')

@bot.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def delete(ctx,member):
    if member in black_list:
        black_list.remove(str(member))
        with open('blacklist.json', 'w') as file:
            json.dump(black_list, file, indent=2, ensure_ascii=False)
            await ctx.send('пользователь не в черном списке')
@bot.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def mute(ctx,member:discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles,name = 'В МУТЕ')
    await member.add_roles(mute_role)
    await ctx.send(f'пользователя {member} замутили')
@bot.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def unmute(ctx,member:discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles,name = 'В МУТЕ')
    await member.remove_roles(mute_role)
    await ctx.send(f'пользователя {member} размутили')

@bot.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def checkbl(ctx):
    message=""
    for item in black_list:
        message = f'{message} {item}\n'
    await ctx.send(message)
tess = []
lives = {}
@bot.command(pass_context = True)
async def game(ctx,integer = None):
    if not integer == None and not str(ctx.author) in tess:
        await ctx.send('вы не начали игру')

    #print(integers[ctx.author.Name])
    if not str(ctx.author) in tess and integer == None:
        integers[str(ctx.author)] = random.randint(1, 10)
        print(integers[str(ctx.author)])
        await ctx.send(f'{ctx.author} , игра начата')
        await ctx.send(f'{ctx.author} , введите число')
        tess.append(str(ctx.author))
        lives[str(ctx.author)] = 5
        print(integers)
        print(tess)

    if str(ctx.author) in tess and not integer == None :
        if int(integer) > integers[str(ctx.author)]:
            await ctx.send('вы ввели число больше')
            lives[str(ctx.author)] = lives[str(ctx.author)] - 1
            if lives[str(ctx.author)] < 1:
                await ctx.send('вы проиграли')
                tess.remove(str(ctx.author))
                integers.pop(ctx.author)

        elif int(integer) < integers[str(ctx.author)]:
            await ctx.send('вы ввели число меньше')
            lives[str(ctx.author)] = lives[str(ctx.author)] - 1
            if lives[str(ctx.author)] < 1:
                await ctx.send('вы проиграли')
                tess.remove(str(ctx.author))
                integers.pop(ctx.author)
                lives.pop(str(ctx.author))

        if int(integer) == integers[str(ctx.author)]:
            await ctx.send('вы выиграли')
            tess.remove(str(ctx.author))
            integers.pop(ctx.author)
            print(integers)

bot.run(config.key)
import discord
import json
from  discord.ext import commands
import config
with open('blacklist.json','r') as file:
    black_listJson = json.load(file)
black_list = black_listJson
print(black_listJson)
print(type(black_list))

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
        if  black_list.extend(member):
            print('member added')

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



bot.run('OTE3NDA0MTM4MDc2MjU4MzM1.Ya4NLw.NjRHDxwmRcoXdrrDPqoPJxffsxo')
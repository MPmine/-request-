import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def Брось_монетку(ctx):
    money = (random.randint(0,2))
    if money == 0:
        await ctx.send(f'Решка')
    else:
        await ctx.send(f'Орел')

@bot.command()
async def Прив_ботик(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """УРААААА у нас новенький!"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("Токен")

import discord
import requests
import os
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
async def Привет_ботик(ctx):
    await ctx.send(f'Привет! Что тебе надобно?')

@bot.command()
async def joined(ctx, member: discord.Member):
    """ УРАА У НАС НОВЕНЬКИЙ!!
        Ну тогда слушай правила!:
        Во первых: ты не должен выражаться нецензурной лексикой!
        Во вторых: даже не думай шутить про членов семьи!!!
        В третьих: Веселись и отдыхай!
        И ещё. Если у тебя есть ещё вопросы или ты просто хочешь узнать что-то о сервере пиши команду: $Бот_расскажи_о_сервере"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def Бот_расскажи_о_сервере(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}! Ты можешь спрашивать меня о чем угодно!!! Выбери любую тему из каталога и напиши ее со знаком: $ в мою личку!')
@bot.command()
async def Правила(ctx):
    await ctx.send(f'''
    Правила сервера таковы: 
        Во первых: ты не должен выражаться нецензурной лексикой!
        Во вторых: даже не думай шутить про членов семьи!!!
        В третьих: Веселись и отдыхай!
        Ну и интересный факт: Создатель любит обижаться)''')
@bot.command()
async def Модерация(ctx):
    await ctx.send(f'''Модеры у нас отборные! Сразу банят тех , кто нарушает правила. 
                Можешь задать им вопрос(только если он реально очень важный) 
                Но все таки советую писать важные вопросы лучше в личку создателю)
                А если ты хочешь узнать как стать модерам , то напиши $Роли''')
@bot.command()
async def Роли(ctx):
    await ctx.send(f'''Привет! И так сразу к ролям.
                   Чтобы стать <глупым крестьянином> достаточно просто написать то, что запрещено на сервере. Уровень этой роли: -10


                   <Главным по ролям> стать возможно только если старый Главный ушел в отставку. Уровень этой роли:?!?!


                   Чтобы стать <Хорошим участником> 
                   нужно принимать участие в играх, проявлять активность и спустя время написать создателю , что вы хотели бы получить данную роль. Уровень этой роли: 5


                   Чтобы стать <Модератором> 
                   нужно принимать участие в играх, проявлять активность и спустя время вас пригласят в специальное место где проверят вашу компитентность на роль модератора. Уровень этой роли: 10


                   Роль <На пути исправления> 
                   получают люди , которые сделали запретную вещь на сервере , но не слишком ужасную(при получении данной роли спустя время можно стать хорошим участником или даже модером). Уровень этой роли: 0.8


                   <Участником> 
                   все становятся просто так, нужно лишь написать <Главному по ролям> Чтобы он дал тебе роль. Уровень этой роли: 1''')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def Ты_Мой_Краш(ctx):
    await ctx.send(f'🥵🥵🥵')


@bot.command()
async def Пупс(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def Скинь_селфи_Игоря(ctx):
    with open('images/mem2.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
    print(os.listdir('images'))
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def Поставь_чела_на_место(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/1158747537826652312/1159057190687092787/7db591e9019c401264592768bba7e2b6.jpg?ex=651e7fa0&is=651d2e20&hm=82c56a33dd465cfbd278a0ca0dfdc37baf4cd1b7d9bd9ee815d2cbcede2b0600&')





def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    '''По команде fox вызывает функцию get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run("Токен")

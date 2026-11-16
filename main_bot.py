import discord
from discord.ext import commands
from bot_logic import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def clave(ctx, longitut):
    longitut = int(longitut)
    await ctx.send(f"tu contraseña segura es: {gen_pass(longitut)}")

@bot.command()
async def moneda(ctx):
    await ctx.send(f'He lanzado la moneda y ha caido: {flip_coin()}')

@bot.command()
async def emoji(ctx):
    await ctx.send(f'Toma tu emoji: {gen_emoji()}')

bot.run("token")

import requests
import discord
import json
from discord.ext import commands
from discord import app_commands
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


#Cotação dolar
url = "https://www.google.com/search?q=cotacao+dolar"
header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
resquisicao = requests.get(url, headers=header)
site = BeautifulSoup(resquisicao.text,"html.parser")

#------

valor = site.find("span", class_="DFlfde SwHCTb")
cotbrl = valor.get_text()
#print(cotbrl)
#------

#Valor BTC
link = "https://www.google.com/search?q=valor+do+bitcoin+dolar"
resquisicao = requests.get(link, headers=header)
site = BeautifulSoup(resquisicao.text,"html.parser")

pesquisa = site.find("span", class_="pclqee")

valor_btc = pesquisa.get_text()
#print(valor_btc)


#Valor ETH
link = "https://www.google.com/search?q=valor+ethereum+em+dolar"
header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
resquisicao = requests.get(link, headers=header)
site = BeautifulSoup(resquisicao.text,"html.parser")


pesquisa = site.find("span", class_="pclqee")
valor_eth = pesquisa.get_text()
#print(valor_eth)

#Valor BNC

link = "https://www.google.com/search?q=valor+binance+coin"
header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
resquisicao = requests.get(link, headers=header)
site = BeautifulSoup(resquisicao.text,"html.parser")


pesquisa = site.find("span", class_="pclqee")

valor_bnc = pesquisa.get_text()

#print(valor_bnc)







@bot.event
async def on_ready():
    #await bot.tree.sync()
    print("Bot pronto!")


#with open("idscordi.txt") as file:
    #meuid = file.read()

@bot.command()
async def sincronizar(ctx:commands.Context):
    if ctx.author.id == "seuid" :
        sincs = await bot.tree.sync()
        await ctx.reply(f"{len(sincs)} comandos sincronizados ")
    else:
        await ctx.reply('Apenas o meu dono pode usar esse comando!')



@bot.command()
async def hello(ctx):
    await ctx.send("hello world")


@bot.tree.command()
async def ola(interact:discord.Interaction):
    await interact.response.send_message(f"Olá,{interact.user.name}")

###cotação
@bot.tree.command(name="cotação")
async def cotacao(interact:discord.Interaction):
    await interact.response.send_message(f"valor do dolar hoje: {cotbrl}")

###Valor btc
@bot.tree.command(name="bitcoin")
async def btc_valor(interact:discord.Interaction):
    await interact.response.send_message(f"bitcoin hoje: {valor_btc}")






##Valores de algumas moedas
@bot.tree.command()
@app_commands.choices(preco=[
    app_commands.Choice(name='bitcoin', value=valor_btc),
    app_commands.Choice(name='etherum', value=valor_eth),
    app_commands.Choice(name='binance coin', value=valor_bnc)
    
])
async def preco(interact:discord.Interaction, preco:app_commands.Choice[str]):
    await interact.response.send_message(f"preço atual: {preco.name} é {preco.value}")




@bot.command()
async def sendembed(ctx):
    embeded_msg = discord.Embed(title="Titulo qualquer",description="Uma descrição qualquer",color=discord.Color.yellow())
    embeded_msg.set_thumbnail(url=ctx.author.avatar)
    embeded_msg.add_field(name="Um nome qualquer", value="Um valor qualquer", inline=False)
    embeded_msg.set_image(url=ctx.guild.icon)
    embeded_msg.set_footer(text="texto de pé(so um texto qualquer)",icon_url=ctx.author.avatar)
    await ctx.send(embed=embeded_msg)


@bot.command()
async def ping_embed(ctx):
    ping_embed = discord.Embed(title="Ping",description="Latency in ms",color=discord.Color.blue())
    ping_embed.add_field(name=f"{bot.user.name}'s Latency (ms): ",value=f"{round(bot.latency * 1000)}ms.",inline=False)
    ping_embed.set_footer(text=f"Requested by {ctx.author.name}.",icon_url=ctx.author.avatar)
    await ctx.send(embed=ping_embed)

with open("config.json") as f:
    configData = json.load(f)

bot.run(configData["token"])
import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json
from datetime import datetime
from pytz import timezone
import os
from dotenv import load_dotenv

if not os.path.exists('birthdays.json'):
    with open('birthdays.json', 'w') as f:
        json.dump({}, f)

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True 
bot = commands.Bot(command_prefix='.', intents=intents)
scheduler = AsyncIOScheduler()

def load_birthdays():
    with open('birthdays.json', 'r') as file:
        return json.load(file)

@bot.event
async def on_ready():
    print(f"bot conectado como {bot.user}")
    scheduler.start()

channel_id = 1397242529472319498  # Replace with your channel ID

@scheduler.scheduled_job("cron", hour=0, minute=0, timezone="America/Sao_Paulo")
async def check_birthdays():
    today = datetime.now(timezone="America/Sao_Paulo")
    today_str = today.strftime("%d-%m")
    birthdays = load_birthdays()

    for user_id, birthday in birthdays.items():
        try:
            birthday_date = datetime.strptime(birthday, "%d-%m-%Y")
        except ValueError:
            continue
        if birthday_date.strftime("%d-%m") == today_str:
            age = today.year - birthday_date.year
            guild = discord.utils.get(bot.guilds)
            channel = guild.get_channel(channel_id)
            if channel:
                user_mention = f"<@{user_id}>"
                try:
                    await channel.send(f"@everyone 🎉 Hoje é aniversário de {user_mention}! Está completando {age} anos! 🎂")    
                except:
                    print(f"Não foi possível enviar mensagem para {channel.name}")

@bot.command()
async def aniversario(ctx, data):
    """
    Comando para o usuário cadastrar o aniversário.
    Exemplo: .aniversario 22-07-2000
    """
    try:
        nascimento = datetime.strptime(data, "%d-%m-%Y")
    except ValueError:
        await ctx.send("❌ Formato inválido. Use: DD-MM-AAAA")
        return

    # Carrega aniversários já cadastrados
    try:
        with open('birthdays.json', 'r') as file:
            birthdays = json.load(file)
    except FileNotFoundError:
        birthdays = {}

    # Salva o aniversário do usuário
    birthdays[str(ctx.author.id)] = data

    # Escreve de volta no arquivo
    with open('birthdays.json', 'w') as file:
        json.dump(birthdays, file, indent=4)

    await ctx.send(f"✅ Aniversário registrado como {data} para {ctx.author.name}!")
    print(f"Comando chamado por {ctx.author} com data {data}")

@bot.command()
async def oi(ctx):
    await ctx.send("Olá!")



bot.run(os.getenv("TOKEN"))
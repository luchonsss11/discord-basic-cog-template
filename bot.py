# Bot main file to import all cogs
import discord 
from discord.ext import commands
import os 
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("PRIVATE")
prefixes = ['!','-','.','?']
bot = commands.Bot(command_prefix=prefixes)

@bot.event
async def on_ready():
    print("i\'m ready!")

bot.load_extension("cog.hey")

bot.run(token)
# Finishes the main file only for cogs
import os

import dotenv
from dotenv import load_dotenv
import disnake
from disnake.ext import commands

load_dotenv()  # Take environment variables from .env.
TOKEN = os.getenv('TOKEN')

bot = commands.Bot()

@bot.event
async def on_ready():
    print("The bot is ready!")

bot.load_extensions("cogs")
bot.run(TOKEN)

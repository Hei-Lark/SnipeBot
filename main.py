import os

import dotenv
from dotenv import load_dotenv
import disnake
from disnake.ext import commands

load_dotenv()  # Take environment variables from .env.
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(test_guilds=[922934220056330271])


@bot.event
async def on_ready():
    print("The bot is ready!")


bot.load_extensions("cogs")
bot.run(TOKEN)

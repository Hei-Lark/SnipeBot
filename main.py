import os

import dotenv
from dotenv import load_dotenv
import disnake
from disnake.ext import commands
import json

load_dotenv()  # Take environment variables from .env.
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(test_guilds=[922934220056330271])


@bot.event
async def on_ready():
    print("The bot is ready!")


bot.load_extensions("cogs")

bot.run(TOKEN)


def reset():
    with open(os.getcwd() + "\\snipeCounts\\CountedUp.json", 'r+') as file:
        count = json.load(file)  # Loads the json file into python
        data = {
            "Array": [
                [0]
            ],
            "TOTALPPL": 1,
            "roster": {
                "260222160272883713": {
                    "Index": 0,
                    "Name": "Cynthia"
                }
            }
        }

    # Sets file's current position at offset.
    file.seek(0)
    # convert back to json.
    json.dump(data, file, indent=4)
    file.close()

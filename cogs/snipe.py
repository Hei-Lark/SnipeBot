import os
from disnake.ext import commands
import disnake
from datetime import datetime
import json
import numpy as np


class SnipeCommand(commands.Cog):
    """This will be for the snipe command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Records Aces snipes.")
    async def snipe(inter, member: disnake.Member):
        sniper = inter.author
        target = member

        # When someone tries to snipe themselves
        if sniper.id == target.id:
            await inter.response.send_message("You can't snipe yourself, silly!")
            return
        # When someone tries to snipe the bot
        elif target.id == 999533372659486820:
            await inter.response.send_message("F*** you, I'm immortal!")
            return
        else:
            # Updates counter of sniped or not.
            write_countUp(sniper, target)

            # Add this event to the LargeLogs.txt
            with open(os.getcwd() + "\\snipeCounts\\LargeLogs.txt", "a") as file:
                file.write("\n")
                file.write(sniper.nick + "(" + str(sniper.id) + ") --->> " + target.nick + "( " + str(target.id) + "), " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

            await inter.response.send_message(sniper.mention + " snip snopped " + target.mention + "!!")
            return


# Used by api to setup existence of this command.
def setup(bot: commands.Bot):
    bot.add_cog(SnipeCommand(bot))


# function to add to JSON
def write_countUp(sniper, target):
    """Documents the logistics that comes with a snipe: Increase sniper's hits by 1 and increases the target's
    been_hit by 1. Increases total snipes by 1.

    Logistics are presented in a nested dictionary, saved in a json file, CountedUp.json."""

    # Fetches sniper and target index
    addTarget = False
    addSniper = False
    with open(os.getcwd() + "\\snipeCounts\\CountedUp.json", 'r+') as file:
        count = json.load(file)  # Loads the json file into python

        # Adds a new user to the roster if they don't exist yet and assigns them a number
        if str(sniper.id) not in count["roster"]:
            addSniper = True
            indexSniper = count["TOTALPPL"]
            count["roster"][sniper.id] = {"Index": indexSniper, "Name": sniper.nick}
            count["TOTALPPL"] += 1
        else:
            indexSniper = count["roster"][str(sniper.id)]["Index"]

        if str(target.id) not in count["roster"]:
            addTarget = True
            indexTarget = count["TOTALPPL"]
            count["roster"][target.id] = {"Index": indexTarget, "Name": target.nick}
            count["TOTALPPL"] += 1
        else:
            indexTarget = count["roster"][str(target.id)]["Index"]

        # Edit the array
        array = np.array(count["Array"])

        if addSniper:
            array = np.lib.pad(array, ((1, 0), (1, 0)))
        if addTarget:
            array = np.lib.pad(array, ((1, 0), (1, 0)))

        array[indexSniper][indexTarget] += 1
        count["Array"] = array.tolist()

        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(count, file, indent=4)
        file.close()
        return

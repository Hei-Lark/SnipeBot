from disnake.ext import commands
import disnake
import json
from openpyxl import load_workbook

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
        elif target == commands.Bot:
            await inter.response.send_message("I'm just a bot :,[")
            return
        else:
            count_and_log(sniper, target)
            await inter.response.send_message(sniper.mention + " sniped " + target.mention + "!")
            return


# Used by api to setup existence of this command.
def setup(bot: commands.Bot):
    bot.add_cog(SnipeCommand(bot))


# function to update body counts
def count_and_log(sniper, target):
    """Documents the logistics that comes with a snipe: Increase sniper's hits by 1 and increases the target's
    been_hit by 1. Increases total snipes by 1.

    Logistics are recorded in a JSON file, each person with a list [snipes, deaths]"""
    
    # update count
    f = open('cogs/snipeCount.json', 'r')
    data = json.load(f)

    # update target death count
    if str(target.id) in data:
        data[str(target.id)]['deaths'] += 1
    else:
        f = open('cogs/snipeCount.json', 'a')
        data.update({target.id:{'snipes':0,'deaths':1}})

    # update sniper snipe count
    if str(sniper.id) in data:
        data[str(sniper.id)]['snipes'] += 1
    else:
        f = open('cogs/snipeCount.json', 'a')
        data.update({sniper.id:{'snipes':1,'deaths':0}})

    f = open('cogs/snipeCount.json', 'w')
    json.dump(data, f)

    f = open('cogs/snipeCount.json', 'r')
    json.load(f)

    f.close()
    return

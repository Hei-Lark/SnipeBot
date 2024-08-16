from disnake.ext import commands
import disnake
import json
from openpyxl import load_workbook
import admin


class FetchCommand(commands.Cog):
    """This will be for the snipe command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Return how many times this person has sniped another person.")
    async def fetchsnipes(inter, member: disnake.Member):
        f = open('cogs/snipeCount.json', 'r')
        data = json.load(f)
        snipes = data[str(member.id)]['snipes']
        print(str(snipes))

        if(str(member.id) in data):
            await inter.response.send_message(member.mention + " has " + str(data[str(member.id)]['deaths']) + " snipes!")
        else:
            await inter.response.send_message(member.mention + " has sniped 0 times!")
        
        f.close()
        return

    @commands.slash_command(description="Returned how many times this person has been sniped (deaths).")
    async def fetchdeaths(inter, member: disnake.Member):
        f = open('cogs/snipeCount.json', 'r')
        data = json.load(f)

        if (str(member.id) in data):
            await inter.response.send_message(member.mention + " has " + str(data[str(member.id)]['deaths']) + " deaths!")
        else:
            await inter.response.send_message(member.mention + " has been sniped 0 times!")
        
        f.close()
        return
    
    @commands.slash_command(description="Returned how many times this person has been sniped (deaths) and sniped others.")
    async def fetchstats(inter, member: disnake.Member):
        f = open('cogs/snipeCount.json', 'r')
        data = json.load(f)

        if (str(member.id) in data):
            await inter.response.send_message(member.mention + " has " + str(data[str(member.id)]['snipes']) + " snipes and " + str(data[str(member.id)]['deaths']) + " deaths!")
        else:
            await inter.response.send_message(member.mention + " has 0 snipes and deaths!")
        
        f.close()
        return
    
    @commands.slash_command(description="Returns list of top three snipers and their scores")
    async def fetchleaderboard(inter):
        admin.updateLeaderboard()

        f = open('cogs/leaderboard.json', 'r')
        data = json.load(f)

        first = "1. (" + str(data["first"]["score"]) + " ) "
        second = "2. (" + str(data["second"]["score"]) + " ) "
        third = "3. (" + str(data["third"]["score"]) + " ) "

        # given list of member IDs, 
        for id in data["first"]["members"]:
            first += commands.Bot.get_user(id).mention + " "

        for id in data["second"]["members"]:
            second += commands.Bot.get_user(id).mention + " "

        for id in data["third"]["members"]:
            third += commands.Bot.get_user(id).mention + " "
        
        f.close()
        await inter.response.send_message(first + "\n" + second + "\n" + third)
        return


def setup(bot: commands.Bot):
    bot.add_cog(FetchCommand(bot))
    return

from disnake.ext import commands
import disnake
import json
from openpyxl import load_workbook


class FetchCommand(commands.Cog):
    """This will be for the snipe command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Return how many times this person has sniped another person.")
    async def fetchbodycount(inter, member: disnake.Member):
        f = open('snipeCount.json', 'r')
        data = json.load(f)
        f.close()
        await inter.response.send_message(member.nick + " has sniped " + data[member.id]['snipes'] + " times!")
        return

    @commands.slash_command(description="Returned how many times this person has been sniped.")
    async def fetchdeaths(inter, member: disnake.Member):
        workbook = load_workbook(filename="snipeCounts/SnipeCount.xlsx")
        countsheet = workbook["counts"]

        f = open('snipeCount.json', 'r')
        data = json.load(f)
        f.close()
        await inter.response.send_message(member.nick + " has been sniped " + data[member.id]['deaths'] + " times!")
        return


def setup(bot: commands.Bot):
    bot.add_cog(FetchCommand(bot))
    return

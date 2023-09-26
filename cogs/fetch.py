from disnake.ext import commands
import disnake
import os
import openpyxl
from openpyxl import load_workbook


class FetchCommand(commands.Cog):
    """This will be for the snipe command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Return how many times this person has sniped another person.")
    async def fetchbodycount(inter, member: disnake.Member):
        workbook = load_workbook(filename="snipeCounts/SnipeCount.xlsx")
        countsheet = workbook["counts"]

        for cell in countsheet["B"]:
            if cell.value == member.id:
                hits = countsheet.cell(row=cell.row, column=3)

        workbook.close()

        await inter.response.send_message(member.nick + " has sniped " + str(hits) + " times!")

    @commands.slash_command(description="Returned how many times this person has been sniped.")
    async def fetchdeaths(inter, member: disnake.Member):
        workbook = load_workbook(filename="snipeCounts/SnipeCount.xlsx")
        countsheet = workbook["counts"]

        for cell in countsheet["B"]:
            if cell.value == member.id:
                been_hit = countsheet.cell(row=cell.row, column=3)

        workbook.close()

        await inter.response.send_message(member.nick + " has been sniped " + str(been_hit) + " times!")
        return


def setup(bot: commands.Bot):
    bot.add_cog(FetchCommand(bot))
    return

import os
from disnake.ext import commands
import disnake
from datetime import datetime
import numpy as np
import openpyxl
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
        elif target.id == 999533372659486820:
            await inter.response.send_message("F*** you, I'm immortal!")
            return
        else:
            count_and_log(sniper, target)

            await inter.response.send_message(sniper.mention + " snip snopped " + target.mention + "!!")

            return


# Used by api to setup existence of this command.
def setup(bot: commands.Bot):
    bot.add_cog(SnipeCommand(bot))


# function to update body counts
def count_and_log(sniper, target):
    """Documents the logistics that comes with a snipe: Increase sniper's hits by 1 and increases the target's
    been_hit by 1. Increases total snipes by 1.

    Logistics are presented in spreadsheet file and edited with openpyxl."""

    workbook = load_workbook(filename="snipeCounts/SnipeCount.xlsx")
    countsheet = workbook["counts"]
    logsheet = workbook["log"]

    # Logs the snipe
    logsheet.insert_rows(idx=2)
    logsheet["A2"] = sniper.nick
    logsheet["B2"] = str(sniper.id)
    logsheet["C2"] = target.nick
    logsheet["D2"] = str(target.id)
    logsheet["E2"] = datetime.now().strftime("%d/%m/%Y")
    logsheet["F2"] = datetime.now().strftime("%H:%M:%S")

    # Update total
    logsheet["H1"] = logsheet.max_row-1

    # seeing if a person exists
    targetExists = False
    sniperExists = False

    # counts up each person's counts
    for cell in countsheet["B"]:
        if cell.value == target.id:
            i = int(countsheet[cell.row][3].value)
            thiscell = countsheet.cell(row=cell.row, column=3)
            thiscell = str(i + 1)
            targetExists = True

        if cell.value == sniper.id:
            i = int(countsheet[cell.row][2].value)
            thiscell = countsheet.cell(row=cell.row, column=2)
            thiscell = str(i + 1)
            sniperExists = True

    if targetExists == False:
        countsheet.append([target.nick, str(target.id), '0', '1'])

    if sniperExists == False:
        countsheet.append([sniper.nick, str(sniper.id), '1', '0'])

    # Save and close worksheet
    workbook.save(filename="snipeCounts/SnipeCount.xlsx")
    workbook.close()

    return

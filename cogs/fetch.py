from disnake.ext import commands
import disnake
import json
import os


class FetchCommand(commands.Cog):
    """This will be for the snipe command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Return how many times this person has successfully sniped another person.")
    async def fetchhits(inter, member: disnake.Member):
        with open(os.getcwd() + "\\snipeCounts\\CountedUp.json", 'r+') as file:
            count = json.load(file)
            array = count["Array"]
            index = count["roster"][str(member.id)]["Index"]

            # Person has been sniped their row
            hits = 0
            for i in range(count["TOTALPPL"]):
                hits += array[index][i]

        await inter.response.send_message(member.nick + " has sniped " + str(hits) + " times!")

    @commands.slash_command(description="Returned how many times this person has been sniped.")
    async def fetchtakeouts(inter, member: disnake.Member):
        with open(os.getcwd() + "\\snipeCounts\\CountedUp.json", 'r+') as file:
            count = json.load(file)
            array = count["Array"]
            index = count["roster"][str(member.id)]["Index"]

            # Person has been sniped their column
            been_hit = 0
            for arr in array:
                been_hit += arr[index]

        await inter.response.send_message(member.nick + " has been sniped " + str(been_hit) + " times!")
        return

    @commands.slash_command(description="Return how many times you have sniped this person.")
    async def fetchtarget(inter, member: disnake.Member):
        with open(os.getcwd() + "\\snipeCounts\\CountedUp.json", 'r+') as file:
            count = json.load(file)
            array = count["Array"]
            indexSniper = count["roster"][str(inter.author.id)]["Index"]
            indexTarget = count["roster"][str(member.id)]["Index"]

        await inter.response.send_message(inter.author.nick + " has sniped " + member.nick + " " + str(array[indexSniper][indexTarget]) + " times!")
        return

def setup(bot: commands.Bot):
    bot.add_cog(FetchCommand(bot))
    return
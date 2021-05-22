import discord
from discord.ext import commands

class helpp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h'])
    async def helpp(self, ctx, args):
        await ctx.send(f"Helped")

def setup(bot):
    bot.add_cog(helpp(bot))
import discord
from discord.ext import commands

class hey(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hy'])
    async def hey(self, ctx, args):
        await ctx.send(f"Hey {args}")

def setup(bot):
    bot.add_cog(hey(bot))
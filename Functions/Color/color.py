import discord
from discord.ext import commands
from .color_final_function import color_main

class colour(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def color(self, ctx):
		file, embed = color_main.RandRGB(discord.Embed, ctx.author, ctx.author.avatar_url, discord.File)
		await ctx.send(file=file, embed=embed)

def setup(bot):
    bot.add_cog(colour(bot))
from random import choice
import datetime
import discord
from discord.ext import commands

class admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(administrator=True)
	@commands.guild_only()	
	async def giveaway(self, ctx, msg=None):
		"""
		Picks a random user from the server to win your giveaway. INSTANT GIVEAWAY!
		"""
		if msg == None:
			embed = discord.Embed(
				title = "You need to name the prize.\n?giveaway [prize name]",
				color = discord.Color.red()
			)
			await ctx.send(embed=embed)
		else:
			winner = choice(ctx.guild.members.mention)
			embed = discord.Embed(
				color = discord.Color.dark_purple(),
				title = f"Prize :: {msg}\nHost :: <@{ctx.author.id}>\nWINNER :: ||{winner}||"
			).set_author(name="INSTANT GIVEAWAY!", icon_url=ctx.author.avatar_url)
			await ctx.send(f"> {winner}", embed=embed)


	@commands.command()
	@commands.has_permissions(administrator=True)
	@commands.guild_only()
	async def ctext(self, ctx, name):
		guild = ctx.message.guild
		if name == None:
			await ctx.send('Sorry, but you have to insert a name. Try again, like this: **`.create [channel name]`**')
		else:
			if name > 100 or name < 1:
				await ctx.send("The channel name must be between 1 and 100 characters long")
			else:
				await guild.create_text_channel(name)
				embed = discord.Embed(title = "Created `{0}`".format(name), color = discord.Color.dark_red()).timestamp = datetime.datetime.utcnow()
				await ctx.send(embed=embed)
	
	@commands.command()
	@commands.has_permissions(administrator=True)
	@commands.guild_only()
	async def cvoice(self, ctx, name):
		guild = ctx.message.guild
		if name == None:
			await ctx.send('Sorry, but you have to insert a name. Try again, like this: **`.create [channel name]`**')
		else:
			if name > 100 or name < 1:
				await ctx.send("The channel name must be between 1 and 100 characters long")
			else:
				await guild.create_voice_channel(name)
				embed = discord.Embed(title = "Created `{0}`".format(name), color = discord.Color.dark_red()).timestamp = datetime.datetime.utcnow()
				await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(admin(bot))

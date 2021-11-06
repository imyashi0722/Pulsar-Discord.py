import random
import datetime
import discord
from discord.ext import commands

class admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(administrator=True)
	@commands.guild_only()	
	async def giveaway(self, ctx, msg):
		"""
		Picks a random user from the server to win your giveaway. INSTANT GIVEAWAY!
		"""
		if msg == None:
			ctx.send("You need to name the prize. Try again, like: **`.giveaway [prize name]`**")
		else:
			embed = discord.Embed(
				title = "INSTANT GIVEAWAY!", 
				color = discord.Color.teal(), 
				description = f"**Prize:** {msg}\n**Hosted by:** {ctx.author}\n**WINNER: ||{random.choice(ctx.guild.members).mention}||**"
			)
			await ctx.send(embed=embed)


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

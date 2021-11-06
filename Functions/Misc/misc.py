import discord
from discord.ext import commands
from discord import Button, ButtonStyle
import datetime

class side_runners():
	def wiki_embed_generator(msg, author):
		embed = discord.Embed(
			title = "Searching '{0}' for {1}".format(msg, author), 
			color=discord.Color.blue(),
			description = "https://en.wikipedia.org/wiki/{0}".format(msg.replace(' ', '_')))
		return embed

class misc(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.command()
	async def wiki(self, ctx, msg=None):
		if msg == None:
			await ctx.send("> `ERROR.` What should I search for?")
		else:
			components = [Button(url="https://en.wikipedia.org/wiki/{0}".format(msg.replace(' ', '_')), label="|| {0}".format(msg.upper()), style=ButtonStyle.url, emoji='🌐')]
			await ctx.send(embed=side_runners.wiki_embed_generator(msg, ctx.author), components=components)
		
	@commands.command()
	async def brokethesentence(self, ctx, sent):
		string: str = ctx.message.content[18:]
		vovels: list = ["a", "A", "e", "E", "u", "U", "o", "O", "i", "I"]
		k: int = -1
		while k < len(string) - 1:
			for i in vovels:
				if string[k] == i:
					string = string.replace(string[k], "")
			k += 1
		await ctx.send(f"The Broken Sentence {string}")

	@commands.command()
	async def length(self, ctx, sent):
		sentence: str = ctx.message.content[7:]
		ctx.send('> **{0}**'.format(sentence))
		lenght: int = len(sentence)
		i = 0
		count: int = 0
		while i < lenght - 1:
			i += 1
			if sentence[i] == " ":
				count += 1
		word = count + 1
		letter = i + 1
		await ctx.send(f"World count : {word}, letter count : {letter}")

	@commands.command()
	async def howoldiam(self, ctx, year):
		now: int = datetime.date.today().year
		author = ctx.author
		print(author)
		try:
			b_year = int(year)
		except ValueError:
			await ctx.send("Please write your birth year.")
		try:
			if 0 < b_year < now:
				age = now - b_year
				await ctx.send("{0} is your age".format(age))
			else:
				await ctx.send("Error.")
		except TypeError:
			await ctx.send("Please write your birth year.")


def setup(bot):
	bot.add_cog(misc(bot))
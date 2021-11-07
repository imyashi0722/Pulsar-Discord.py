import discord
from discord.ext import commands
from discord import Button, ButtonStyle
import datetime
from PIL import Image
import requests
from io import BytesIO

from settings import BotID

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
	async def length(self, ctx, sent=None):
		sentence: str = ctx.message.content[7:]
		if len(sentence) >= 1:
			await ctx.send('> **{0}**'.format(sentence))
			lenght: int = len(sentence)
			i = 0
			count: int = 0
			while i < lenght - 1:
				i += 1
				if sentence[i] == " ":
					count += 1
			word = count + 1
			letter = i

			embed = discord.Embed(
				title = "Word count :: {0}\nLetter count :: {1}".format(word, letter),
				color = discord.Color.green()
			)
		else:
			embed = discord.Embed(
				title = "Please enter some text",
				color = discord.Color.red()
			)
		await ctx.send(embed=embed)

	@commands.command()
	async def myage(self, ctx, year):
		now: int = datetime.date.today().year
		try:
			b_year = int(year)
		except ValueError:
			embed = discord.Embed(
				title = "Please write your birth year.",
				color = discord.Color.red()
			)
			await ctx.send(embed=embed)
		try:
			if 0 < b_year < now:
				age = now - b_year
				embed = discord.Embed(
					title = "You are {0} year old!".format(age),
					color = discord.Color.gold()
				)
				await ctx.send(embed=embed)
			else:
				age = now - b_year
				embed = discord.Embed(
					title = "odd...\n{0} years old??\nPlease enter a proper Y.O.B".format(age),
					color = discord.Color.red()
				)
				await ctx.send(embed=embed)
		except TypeError:
			embed = discord.Embed(
				title = "Please write your birth year.",
				color = discord.Color.red()
			)
			await ctx.send(embed=embed)
	
"""	@commands.command()
	async def impost(self, ctx, user: discord.User, *, msg=None):
		if isinstance(user, commands.MissingRequiredArgument):
			embed = discord.Embed(
				title = "You have either forgotten to mention someone or you forgot to add text.",
				color = discord.Color.red()
			).set_author(name = ctx.message.content, icon_url = ctx.author.avatar_url)
			await ctx.send(embed=embed)
		else:
			client = commands.Bot
			response = requests.get(user.avatar_url)
			img = Image.open(BytesIO(response.content))
			await client.user.edit(avatar=img)
			await ctx.send(msg)"""

def setup(bot):
	bot.add_cog(misc(bot))
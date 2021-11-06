import discord
from discord.ext import commands
import datetime
import random

import settings 

class side_runners():
	def random_hex():
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)
		hex = '0x%02x%02x%02x' % (R, G, B)
		hexa = int(hex, (16))
		return hexa

	def info_embed_generator(ava):
		embed = discord.Embed(
            title="Pulsar",
            description="This bot made by <@{744482789088296980}>",
            colour=discord.Colour.teal()
        )
		embed.set_footer(text="Prefix :: {0}".format(settings.Prefix), icon_url=ava)
		embed.set_author(name='SlepyCot.', icon_url="https://cdn.discordapp.com/avatars/744482789088296980/2ef45914557e7f021fa89eaf9c1ecd1b.png?size=4096")
		embed.add_field(name="Commands", value="Type .help for commands.", inline=True)
		return embed

	def avatar_embed_generator(user, author):
		embed = discord.Embed(title = user.name, color = side_runners.random_hex())
		embed.set_author(name = author, icon_url = author.avatar_url)
		embed.set_image(user.avatar_url)
		return embed

	def help_embed_generator(ava):
		embed = discord.Embed(title="Pulsar", color = discord.Color.red())
		embed.set_footer(text=f"{settings.BotStatus}, Prefix :: {settings.Prefix}", icon_url=ava)
		embed.set_author(name='SlepyCot.', icon_url="https://cdn.discordapp.com/avatars/744482789088296980/2ef45914557e7f021fa89eaf9c1ecd1b.png?size=4096")
		embed.add_field(name=f"{settings.Prefix}ping", value="The bot latency.", inline=False)
		embed.add_field(name=f"{settings.Prefix}time", value="Current time(in UTC).", inline=False)
		embed.add_field(name=f"{settings.Prefix}avatar", value="Shows your avatar.", inline=False)
		embed.add_field(name=f"{settings.Prefix}info", value="Info about bot.", inline=False)
		embed.add_field(name=f"{settings.Prefix}coinflip", value="CoinFlip game.", inline=False)
		embed.add_field(name=f"{settings.Prefix}joke", value="Makes a joke.", inline=False)
		embed.add_field(name=f"{settings.Prefix}mirror", value="Bot mirrors your sentence.", inline=False)
		embed.add_field(name=f"{settings.Prefix}giveaway", value='Only who has "Admin" role can use this command.', inline=False)
		embed.add_field(name=f"{settings.Prefix}brokethesentence", value='Brokes the sentence.', inline=False)
		embed.add_field(name=f"{settings.Prefix}lenght", value='Gives you info about the sentence.', inline=False)
		embed.add_field(name=f"{settings.Prefix}minecraft", value='Shows your minecraft profile.', inline=False)
		embed.add_field(name=f"{settings.Prefix}writinggame", value='Game for fast writing.', inline=False)
		embed.add_field(name=f"{settings.Prefix}wiki", value='Send you the wiki link of requested thing.', inline=False)
		return embed

class info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.command()
	async def info(self, ctx):
		await ctx.send(embed=side_runners.info_embed_generator(self.Bot.avatar_url))

	@commands.command()
	async def ping(self, ctx):
		t = await ctx.send('Pong!')
		ms = (t.created_at-ctx.message.created_at).total_seconds() * 1000
		await t.edit(content='Pong! {0}ms'.format(int(ms)))

	@commands.command()
	async def time(self, ctx):
		await ctx.send('> The time is: **{0} UTC**'.format(datetime.datetime.now().strftime('%H:%M:%S %d/%m/%Y')))

	@commands.command()
	async def avatar(self, ctx, user: discord.User):
		user = user or ctx.author
		await ctx.send(embed=side_runners.avatar_embed_generator(user, ctx.author))

	@commands.command()
	async def help(self, ctx):
		await ctx.send(embed=side_runners.help_embed_generator(self.Bot.avatar_url))

def setup(bot):
	bot.add_cog(info(bot))

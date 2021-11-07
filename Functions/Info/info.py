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
		embed.set_image(url=user.avatar_url)
		return embed

class info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.command()
	async def info(self, ctx):
		Bot = '895996523421261884'
		await ctx.send(embed=side_runners.info_embed_generator(Bot.user.avatar_url))

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

def setup(bot):
	bot.add_cog(info(bot))
import discord
from discord.ext import commands
from discord.errors import Forbidden
from settings import Prefix

"""This custom help command is a perfect replacement for the default one on any Discord Bot written in Discord.py!
However, you must put "bot.remove_command('help')" in your bot, and the command must be in a cog for it to work.
Original concept by Jared Newsom (AKA Jared M.F.)
[Deleted] https://gist.github.com/StudioMFTechnologies/ad41bfd32b2379ccffe90b0e34128b8b
Rewritten and optimized by github.com/nonchris
https://gist.github.com/nonchris/1c7060a14a9d94e7929aa2ef14c41bc2
You need to set three variables to make that cog run.
Have a look at line 51 to 57
"""


async def send_embed(ctx, embed):
	"""
	Function that handles the sending of embeds
	-> Takes context and embed to send
	- tries to send embed in channel
	- tries to send normal message when that fails
	- tries to send embed private with information abot missing permissions
	If this all fails: https://youtu.be/dQw4w9WgXcQ
	"""
	try:
		await ctx.send(embed=embed)
	except Forbidden:
		try:
			await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
		except Forbidden:
			await ctx.author.send(
				f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
				f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Help(commands.Cog):
	"""
	Sends this help message
	"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.bot_has_permissions(add_reactions=True,embed_links=True)
	async def help(self, ctx, *input):
		"""Shows all modules of that bot"""
		prefix = Prefix
		version = "v2.0"
		owner = 744482789088296980
		owner_name = 'SlepyCot.#3578'

		if not input:
			try:
				owner = ctx.guild.get_member(owner).mention
			except AttributeError as e:
				owner = owner
				
			embed = discord.Embed(
				title='Commands and modules', 
				color=discord.Color.teal(),
				description=f'Use `{prefix}help <module>` to gain more information about that module :smiley:\n'
			).set_footer(text=f"Bot is running on version :: {version}")

			cogs_desc = ''
			for cog in self.bot.cogs:
				cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

			embed.add_field(name='Modules', value=cogs_desc, inline=False)

			commands_desc = ''
			for command in self.bot.walk_commands():
				if not command.cog_name and not command.hidden:
					commands_desc += f'{command.name} - {command.help}\n'

			if commands_desc:
				embed.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

			embed.add_field(
				name="About", 
				value=f"The Bots is developed by {owner_name}, based on `discord.py`.\n\
						This version of it is maintained by {owner}\n\
						Please visit https://github.com/imyashi0722/Pulsar-Discord.py to submit ideas or bugs.")

		elif len(input) == 1:
			for cog in self.bot.cogs:
				if cog.lower() == input[0].lower():
					embed = discord.Embed(
						title=f'{cog} - Commands', 
						description=self.bot.cogs[cog].__doc__,
						color=discord.Color.green()
					)

					for command in self.bot.get_cog(cog).get_commands():
						if not command.hidden:
							embed.add_field(
								name=f"`{prefix}{command.name}`", 
								value=command.help, inline=False
							)
					break

			else:
				embed = discord.Embed(
					title="What's that?!",
					description=f"I've never heard from a module called `{input[0]}` before :scream:",
					color=discord.Color.red()
				)

		elif len(input) > 1:
			embed = discord.Embed(
				title="That's too much.",
				description="Please request only one module at once :sweat_smile:",
				color=discord.Color.red()
			)

		else:
			embed = discord.Embed(
				title="It's a magical place.",
				description="I don't know how you got here. But I didn't see this coming at all.\n"
							"Would you please be so kind to report that issue to me on github?\n"
							"https://github.com/imyashi0722/Pulsar-Discord.py\n"
							"Thank you! ~{0}".format(owner_name),
				color=discord.Color.red()
			).set_thumbnail(url='https://www.pinclipart.com/picdir/middle/31-312251_laughter-images-transparent-pluspng-crying-laughing-emoji-discord.png')

		await send_embed(embed=embed)


def setup(bot):
	bot.add_cog(Help(bot))
import discord
from discord.ext import commands

class side_runners():
	def embed_generator(guild, author):
		embed = discord.Embed(
			color = 'RANDOM',
			title = "Welcome to {0} {1}".format(guild.name, author.name)
		)
		embed.set_author(guild.name, guild.icon_url)
		embed.set_thumbnail(author.avatar_url)
		return embed

class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None: await channel.send(embed=side_runners.embed_generator(member.guild, member))


def setup(bot):
    bot.add_cog(welcome(bot))

import discord
from discord.ext import commands
import requests
import json

class side_runners():
	def get_quote(self):
		response = requests.get("https://zenquotes.io/api/random")
		json_data = json.loads(response.text)

		if "Obtain an auth key for unlimited access. - zenquotes.io" in json_data[0]['q']:
			embed = discord.Embed(
				title = "Hey! slow down, or i shall be spinning too fast to exist :("
			)
			embed.set_author(name = self.user.name, icon_url = self.user.avatar_url)
		else:
			embed = discord.Embed(
				title = json_data[0]['a'],
				description = "**{0}**".format(json_data[0]['q'])
			)
			embed.set_thumbnail("https://i.postimg.cc/SRkM97Yh/quotes.jpg")

		return embed

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def quote(self, ctx):
        ctx.send(side_runners.get_quote(self.bot))

    @commands.command()
    async def mirror(self, ctx, message):
        await ctx.send(message)


def setup(bot):
    bot.add_cog(fun(bot))
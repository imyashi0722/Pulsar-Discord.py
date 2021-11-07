import random
import discord
from discord.ext import commands

class side_runners():
	def writing_game(sentence_to_write):
		from PIL import Image, ImageDraw

		img = Image.new('RGB', (1600, 80), color=(73, 109, 137))
		d = ImageDraw.Draw(img)
		d = ImageDraw.Draw(img)
		from PIL import ImageFont
		fnt = ImageFont.truetype('arial.ttf', 38)
		d.text((20, 20), "{0}".format(sentence_to_write), font=fnt, fill=(255, 255, 0))
		img.save("pil_text_font.png")

		embed = discord.Embed(title = "Sentence you need to write : ", color = discord.Colour.gold())
		embed.Image(file=discord.File("pil_text_font.png"))
		return embed

	def coinflip_flip(author):
		embed = discord.Embed(title = "Heads" if random.randint(1, 2) == 1 else "Tails")
		embed.set_author(author.name, author.avatar_url)
		return embed

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    isgameactive = 0

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.isgameactive == 1:
            global sentence_to_write
            if sentence_to_write == ctx.content:
                await ctx.channel.send("{0} won the game !".format(ctx.author))
                self.isgameactive = 0

    Sentences = ["The quick brown fox jumps over the lazy dog.", "The cat went meow as Ms.Longbottom walked in."]
    sentence_to_write = ""

    @commands.command()
    async def writinggame(self, ctx):
        self.isgameactive
        if self.isgameactive == 0:
            global sentence_to_write
            sentence_to_write = self.Sentences[random.randint(0, len(self.Sentences))]
            embed = side_runners.writing_game(sentence_to_write)
            await ctx.send(embed=embed)
            self.isgameactive = 1
        else:
            await ctx.send("Game is being played now, you can only play one game at a time!!")

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send(embed=side_runners.coinflip_flip(ctx.author))


def setup(bot):
    bot.add_cog(Games(bot))

import os
os.system("pip install -r requirements.txt")

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import settings
from server import keep_alive

intents = discord.Intents.default()

cogs: list = ["Functions.Fun.games", "Functions.Fun.gameinfos", "Functions.Fun.otherfuncommands", "Functions.Info.info",
        "Functions.Misc.misc", "Functions.NewMember.newmember", "Functions.Admin.admin", "Functions.Color.color"]

client = commands.Bot(command_prefix=commands.when_mentioned_or(settings.Prefix), case_insensitive=True, help_command=None, intents=intents)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@client.event
async def on_ready():
	print("Bot is ready!")

	channel = 904357053731078245
	channel = client.get_channel(channel)
	await channel.connect()
	print("connected to discord channel :: #{0} ({1})".format(channel.id, channel))

	await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
	for cog in cogs:
		try:
			print(f"📦 Loading cog {cog}")
			client.load_extension(cog)
			print(f"✅ Loaded cog {cog}")
		except Exception as e:
			exc = "{0}: {1}".format(type(e).__name__, e)
			print("❌ Failed to load cog {0}\n>>> {1}".format(cog, exc))

keep_alive()
client.run(os.environ['TOKEN'])
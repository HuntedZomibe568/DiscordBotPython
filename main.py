import discord
import os
from discord import app_commands
from discord.ext import commands
from webserver import keep_alive

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="test")
async def test(interaction: discord.interactions):
    await interaction.response.send_message("This is a test command")


token = os.environ.get("TOKEN")
keep_alive()
if token is not None:
    bot.run(token)
else:
    print("Please set the token in 'TOKEN' enviorment varible")
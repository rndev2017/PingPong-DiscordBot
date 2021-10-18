import constants as consts
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("Awaiting commands...")

@bot.command()
async def ping(ctx):
    author: str = ctx.author.display_name
    await ctx.send(f"🏓 Pong! for {author} 🏓")
    
bot.run(consts.DISCORD_TOKEN)
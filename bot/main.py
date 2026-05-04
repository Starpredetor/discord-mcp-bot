import discord
from discord.ext import commands
import asyncio
import dotenv
import os


dotenv.load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
intents = discord.Intents.default()


bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"Bot successfully logged in as {bot.user.name}")


@bot.slash_command()
async def ping(ctx: discord.ApplicationContext):
    """Basic Ping command that shows the bots latancy"""
    await ctx.respond(f"The currenty latency is {round(bot.latency*1000, 2)}ms")


bot.run(TOKEN)
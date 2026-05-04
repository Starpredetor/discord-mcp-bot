import discord
from discord.ext import commands
import asyncio
import dotenv
import os
from bot.interactions.views import ApprovalView
from bot.services.mcp_client import MCPClient

dotenv.load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
intents = discord.Intents.default()

mcp = MCPClient()

bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"Bot successfully logged in as {bot.user.name}")


@bot.slash_command()
async def ping(ctx: discord.ApplicationContext):
    """Basic Ping command that shows the bots latancy"""
    await ctx.respond(f"The currenty latency is {round(bot.latency*1000, 2)}ms")

#TEMP testing commands

@bot.slash_command(name="test_delete")
async def test_delete(ctx):
    await ctx.respond("MCP SERVER TEST MESSAGE WILL BE DELETED IN `5 SECONDS`.....")
    msg = await ctx.interaction.original_response()
    await asyncio.sleep(5)
    res = await mcp.execute(
        "MESSAGE_DELETE",
        {
            "channel_id" : str(ctx.channel.id),
            "message_id" : str(msg.id)
        }
    )
    print(res)
    if res.get("status") == "approval_required":
        view = ApprovalView(mcp, res["request_id"])

        await ctx.followup.send(f"Approval required for {res['route']}", view=view)
        
    elif "error" in res:
        await ctx.followup.send(f"Error: {res["error"]}")
    else:
        await ctx.followup.send("Executed Successfully!") 

bot.run(TOKEN)
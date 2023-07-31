import os
import discord
import openai
import re

from discord.ext import commands
from discord.channel import TextChannel

from gptcord import activities, gpt_client
from gptcord.views import InviteView, ImageView, InviteQueryView

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
activities.register_commands(bot)

@bot.event
async def on_ready():
    print("Bot ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        prompt = re.sub(r'<@(.*?)>', "", message.content).strip()
        reply = gpt_client.completion(prompt).strip()

        await message.reply(reply)

@bot.event
async def on_voice_state_update(member, before, after):
    # We only want to catch when a user initially joins
    if before.channel is not None or after.channel is None:
        return

    channel_to_alert = after.channel

    if len(channel_to_alert.members) != 1:
        return
    
    await channel_to_alert.send(content="Would you like to invite anyone?", delete_after=(60), view=InviteQueryView(), silent=True)

@bot.slash_command(name="invite")
async def invite(ctx, game_name):
    embed = discord.Embed(
        title=f"{ game_name }",
        description=f"@here",
        color=discord.Color.red()
    )
    embed.set_author(
        name=ctx.author.display_name,
        icon_url=ctx.author.display_avatar
    )

    await ctx.respond(embed=embed, view=InviteView())

@bot.slash_command(name="image")
async def image(ctx, prompt):
    if hasattr(ctx, "defer"):
        await ctx.defer()
    
    image_url, cost = gpt_client.image(prompt)
    embed = discord.Embed()
    embed.set_image(url=image_url)

    if hasattr(ctx, "respond"):
        await ctx.respond(f"That cost **${cost}**. Was it worth it?", embed=embed, view=ImageView())
    else:
        await ctx.followup.send(f"That cost **${cost}**. Was it worth it?", embed=embed, view=ImageView())

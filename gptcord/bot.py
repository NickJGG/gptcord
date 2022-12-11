import os
import discord
import openai
import re

from discord.ext import commands

from . import activities

OPENAI_SECRET_KEY = os.environ.get("OPENAI_SECRET_KEY", "")
CHAT_TEMPERATURE = float(os.environ.get("CHAT_TEMPERATURE", 0))
CHAT_MAX_TOKENS = int(os.environ.get("CHAT_MAX_TOKENS", 50))

openai.api_key = OPENAI_SECRET_KEY

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
        reply = get_reply(prompt).strip()

        await message.reply(reply)

def get_reply(message):
    replies = openai.Completion.create(model="text-davinci-003", prompt=message, temperature=CHAT_TEMPERATURE, max_tokens=CHAT_MAX_TOKENS)
    reply = replies["choices"][0]["text"]

    return reply
        
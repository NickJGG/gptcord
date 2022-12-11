import os

from dotenv import load_dotenv
load_dotenv()

from gptcord import bot

if __name__ == "__main__":
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    bot.run(BOT_TOKEN)

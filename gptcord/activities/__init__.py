from .activity import Activity
from .number_guess import NumberGuess
from .word_scramble import WordScramble
from .word_guess import WordGuess

import discord

ACTIVITIES = {
    NumberGuess,
    WordGuess,
    WordScramble
}

def register_commands(bot):
    group = discord.SlashCommandGroup("activity", "Activities generated using OpenAI's ChatGPT")

    for activity in ACTIVITIES:
        @group.command(name=activity.COMMAND, description=activity.DESCRIPTION)
        async def command(ctx):
            return await activity(bot, ctx).play()
    
    bot.add_application_command(group)

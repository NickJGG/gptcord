import asyncio
import random

from .activity import Activity, WORDS

class WordScramble(Activity):
    NAME = "Word Scramble"
    DESCRIPTION = "Unscramble letters to find the word the bot is thinking of"
    COMMAND = "wordscramble"

    async def play(self):
        word = random.choice(WORDS)
        scrambled_word = scramble_word(word)

        # Send the scrambled word to the channel
        await self.message.channel.send(f"Word Scramble: {scrambled_word}")

        # Wait for players to guess the word
        def guess_check(message):
            return message.content.lower() == word.lower()
        try:
            guess = await self.bot.wait_for("message", check=guess_check, timeout=60.0)
        except asyncio.TimeoutError:
            # If no one guesses the word within the time limit, reveal the answer
            await self.message.channel.send(f"Time's up! The correct word was: {word}")
        else:
            # If someone guesses the word, announce the correct answer and the name of the player who guessed it
            await self.message.channel.send(f"{guess.author.mention} guessed the correct word: {word}")

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    
    return "".join(word)

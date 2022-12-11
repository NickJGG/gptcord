import random

from .activity import Activity

class NumberGuess(Activity):
    NAME = "Number Guess"
    DESCRIPTION = "Guess what number the bot is thinking of"
    COMMAND = "numberguess"

    async def play(self):
        # generate a random number between 1 and 10
        number = random.randint(1, 10)
        
        # ask the user to guess the number
        await self.message.channel.send("I'm thinking of a number between 1 and 10. Can you guess what it is?")
        
        # wait for the user's response
        response = await self.bot.wait_for('message', check=lambda m: m.author == self.message.author)
        
        # check if the user's guess is correct
        if int(response.content) == number:
            await self.message.channel.send("You got it! Good job!")
        else:
            await self.message.channel.send(f"Sorry, the correct number was {number}. Better luck next time!")

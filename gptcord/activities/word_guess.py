import random

from .activity import Activity, WORDS

class WordGuess(Activity):
    NAME = "Word Guess"
    DESCRIPTION = "Guess what word the bot is thinking of"
    COMMAND = "wordguess"

    async def play(self):
        word = random.choice(WORDS)
        
        # initialize a list of underscores to represent the letters in the word
        hidden_word = ["_" for _ in word]
        
        # keep track of the number of incorrect guesses
        incorrect_guesses = []
        allowed_incorrect_guesses = 5
        
        while True:
            # print the current state of the hidden word
            hidden_word_str = f"`{' '.join(hidden_word)}`"

            displayed_incorrect_guesses = ' '.join(incorrect_guesses if len(incorrect_guesses) != 0 else [" "])
            message = f"""
                **Correct Guesses** \t\t\t\t\t{ hidden_word_str } \nIncorrect Guesses ({ len(incorrect_guesses) }/{ allowed_incorrect_guesses }) \t\t`{ displayed_incorrect_guesses }`
            """

            await self.message.channel.send(message)
            
            # ask the user to guess a letter
            await self.message.channel.send("\n\nGuess a letter:")
            
            # wait for the user's response
            response = await self.bot.wait_for('message', check=lambda m: m.author == self.message.author)
            guess = response.content

            # check if the letter is in the word
            if guess in word:
                # reveal the letter in the hidden word
                for i in range(len(word)):
                    if word[i] == guess:
                        hidden_word[i] = guess
                
                # check if the user has won
                if "_" not in hidden_word:
                    await self.message.channel.send(f"You got it! Good job! The word was `{word}`")
                    break
            else:
                # increment the number of incorrect guesses
                incorrect_guesses.append(guess)
                
                # check if the user has lost
                if len(incorrect_guesses) >= allowed_incorrect_guesses:
                    await self.message.channel.send(f"Sorry, you ran out of guesses. The word was `{word}`. Better luck next time!")
                    break

import discord

from gptcord import gpt_client

class ImageView(discord.ui.View):
    @discord.ui.button(label="Regenerate", style=discord.ButtonStyle.success)
    async def accept_callback(self, button, interaction):
        await gpt_client.image(interaction, interaction.message.clean_content)

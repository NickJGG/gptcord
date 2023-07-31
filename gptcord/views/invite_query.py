import discord

from gptcord.modals import InviteModal, GameModal
from gptcord.views import InviteView

class InviteQueryView(discord.ui.View):
    def embed_response(self, interaction, action):
        embed = discord.Embed(description=action)
        embed.set_author(
            name=f"{interaction.user.display_name} has invited you to join",
            icon_url=interaction.user.display_avatar
        )

        return embed

    @discord.ui.button(label="#rocket-league-bois", style=discord.ButtonStyle.primary)
    async def rocket_league_bois(self, button, interaction):
        await interaction.response.send_modal(GameModal("rocket-league-bois", title="Invite"))

    @discord.ui.button(label="#siege-bois", style=discord.ButtonStyle.primary)
    async def siege_bois(self, button, interaction):
        await interaction.response.send_modal(GameModal("siege-bois", title="Invite"))

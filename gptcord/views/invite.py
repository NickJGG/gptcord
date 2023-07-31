import discord

from gptcord.modals import InviteModal

class InviteView(discord.ui.View):
    def embed_response(self, interaction, action, color):
        embed = discord.Embed(
            #title=action,
            color=color,
        )
        embed.set_author(
            name=f"{interaction.user.display_name} {action}",
            icon_url=interaction.user.display_avatar,
        )

        return embed

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success)
    async def accept_callback(self, button, interaction):
        action = "accepted"
        color = discord.Color.green()

        await interaction.response.send_message(embeds=[self.embed_response(interaction, action, color)], delete_after=30*60)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.danger)
    async def deny_callback(self, button, interaction):
        action = "denied"
        color = discord.Color.red()

        await interaction.response.send_message(embeds=[self.embed_response(interaction, action, color)], delete_after=30*60)

    @discord.ui.button(label="Give me...", style=discord.ButtonStyle.primary)
    async def other_callback(self, button, interaction):
        await interaction.response.send_modal(InviteModal(title="Other"))

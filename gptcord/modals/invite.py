import discord

class InviteModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="I can be on in.."))

    async def callback(self, interaction: discord.Interaction):
        time = self.children[0].value

        embed = discord.Embed(color=discord.Color.blue())
        embed.set_author(
            name=f"{interaction.user.display_name} can be on in {time}",
            icon_url=interaction.user.display_avatar
        )
        
        await interaction.response.send_message(embeds=[embed], delete_after=30*60)

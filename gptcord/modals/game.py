import discord

class GameModal(discord.ui.Modal):
    def __init__(self, channel_name, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.channel_name = channel_name

        self.add_item(discord.ui.InputText(label="Game"))


    async def callback(self, interaction: discord.Interaction):
        game_name = self.children[0].value
        
        embed = discord.Embed(
            title=game_name,
            description=f"@here",
            color=discord.Color.blue()
        )
        embed.set_author(
            name=interaction.user.display_name,
            icon_url=interaction.user.display_avatar
        )

        from gptcord.views import InviteView

        message = await discord.utils.get(interaction.channel.guild.channels, name=self.channel_name).send(embed=embed, view=InviteView(), delete_after=30*60)
        await interaction.response.send_message(content=f":point_right: {message.to_reference().jump_url}", ephemeral=True, delete_after=30*60)

    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a Flavor!", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Strawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")

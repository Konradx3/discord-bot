import discord


class EnchantDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="0", value='0'),
            discord.SelectOption(label="1", value='LEVEL1@1'),
            discord.SelectOption(label="2", value='LEVEL2@2'),
            discord.SelectOption(label="3", value='LEVEL3@3'),
            discord.SelectOption(label="4", value='LEVEL4@4'),
        ]

        super().__init__(placeholder="Wybierz stopień zaklęcia surowca", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await self.view.update_selection('enchant', self.values[0], self.options)
        await self.view.check_complete(interaction)

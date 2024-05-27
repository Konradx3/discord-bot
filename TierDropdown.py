import discord


class TierDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="T1", value='T1'),
            discord.SelectOption(label="T2", value='T2'),
            discord.SelectOption(label="T3", value='T3'),
            discord.SelectOption(label="T4", value='T4'),
            discord.SelectOption(label="T5", value='T5'),
            discord.SelectOption(label="T6", value='T6'),
            discord.SelectOption(label="T7", value='T7'),
            discord.SelectOption(label="T8", value='T8'),
        ]

        super().__init__(placeholder="Wybierz Tier surowca", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await self.view.update_selection('tier', self.values[0], self.options)
        await self.view.check_complete(interaction)

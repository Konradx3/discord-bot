import discord


class ResourceDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Witułka", value='FIBER', emoji='<:fiber:1244286748427817044>'),
            discord.SelectOption(label="Materiał", value='CLOTH', emoji='<:cloth:1244286746666209381>'),
            discord.SelectOption(label="Surowa skóra", value='HIDE', emoji='<:hide:1244286749593698305>'),
            discord.SelectOption(label="Skóra", value='LEATHER', emoji='<:leather:1244286751510499508>'),
            discord.SelectOption(label="Ruda", value='ORE', emoji='<:ore:1244286754819670106>'),
            discord.SelectOption(label="Sztabka rudy", value='METALBAR', emoji='<:metalbar:1244286753221644329>'),
            discord.SelectOption(label="Kamień", value='STONE', emoji='<:stone:1244286758003146885>'),
            discord.SelectOption(label="Blok kamienny", value='STONEBLOCK', emoji='<:stoneblock:1244286759320424549>'),
            discord.SelectOption(label="Drewno", value='WOOD', emoji='<:wood_logs:1244286807009525811>'),
            discord.SelectOption(label="Deski", value='PLANK', emoji='<:planks:1244286756392669224>'),
        ]

        super().__init__(placeholder="Zaznacz surowiec", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await self.view.update_selection('resource', self.values[0], self.options)
        await self.view.check_complete(interaction)
